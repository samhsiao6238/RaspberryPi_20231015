#!/bin/bash

# 加載 .env 文件中的環境變量
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# LineNotify Token
# TOKEN=""

# 發送通知的函數
send_line_notify() {
    local message=$1
    curl -X POST -H "Authorization: Bearer $TOKEN" -F "message=$message" https://notify-api.line.me/api/notify
}

# 等待網路接口初始化
sleep 20

# 初始化通知訊息變量
# 預設已經有表頭 【樹莓派開機通知】
notification_message=$(cat << EOF

開始檢查網路介面狀態...

EOF
)

# 檢查網路接口狀態
eth0_status=$(nmcli device status | grep -E "^eth0\s" | awk '{print $3}')
wlan0_status=$(nmcli device status | grep -E "^wlan0\s" | awk '{print $3}')

# 添加接口狀態到通知訊息
notification_message+=$(cat << EOF

eth0 status: $eth0_status
wlan0 status: $wlan0_status

EOF
)

# 檢查並連接到教室網路
if ping -c 1 -W 1 172.16.4.1 &> /dev/null; then
    notification_message+=$(cat << EOF

偵測到教室網路，

EOF
)
    sudo nmcli connection modify "WC1" ipv4.addresses 172.16.4.35/24
    sudo nmcli connection modify "WC1" ipv4.gateway 172.16.4.1
    sudo nmcli connection modify "WC1" ipv4.dns "8.8.8.8 8.8.4.4"
    sudo nmcli connection down "WC1"
    sudo nmcli connection up "WC1"
    IP=$(ip -4 addr show dev eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
    notification_message+=$(cat << EOF

透過 IP 連線：$IP

EOF
)

# 檢查並連接到家庭有線網路
elif ping -c 1 -W 1 192.168.1.1 &> /dev/null && [ "$eth0_status" = "已連線" ]; then
    notification_message+=$(cat << EOF

偵測到的家庭有線網路，

EOF
)
    sudo nmcli connection modify "WC1" ipv4.addresses 192.168.1.149/24
    sudo nmcli connection modify "WC1" ipv4.gateway 192.168.1.1
    sudo nmcli connection modify "WC1" ipv4.dns "8.8.8.8 8.8.4.4"
    sudo nmcli connection down "WC1"
    sudo nmcli connection up "WC1"
    IP=$(ip -4 addr show dev eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
    notification_message+=$(cat << EOF
透過固定 IP 連線：$IP

EOF
)

# 檢查並連接到家庭無線網路
elif ping -c 1 -W 1 192.168.1.1 &> /dev/null && [ "$wlan0_status" = "已連線" ]; then
    notification_message+=$(cat << EOF

偵測到的家庭無線網路，

EOF
)
    sudo nmcli connection modify "SamHome" ipv4.addresses 192.168.1.150/24
    sudo nmcli connection modify "SamHome" ipv4.gateway 192.168.1.1
    sudo nmcli connection modify "SamHome" ipv4.dns "8.8.8.8 8.8.4.4"
    sudo nmcli connection down "SamHome"
    sudo nmcli connection up "SamHome"
    IP=$(ip -4 addr show dev wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
    notification_message+=$(cat << EOF
透過固定 IP 連線：$IP

EOF
)

else
    notification_message+=$(cat << EOF

未找到已知網路。

EOF
)
fi

# 發送合併的通知訊息
send_line_notify "-> $notification_message"
