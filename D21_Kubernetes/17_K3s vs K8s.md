# K3s vs K8S 

_兩者是同一個核心技術的不同實現_

## 目標用途

1. K8S (Kubernetes): 設計用於企業級的大規模容器編排，適合運行在資源豐富的數據中心和雲環境中。提供豐富的功能和擴展性，適用於複雜的應用部署和管理。

2. K3s: 由 Rancher Labs 開發，針對資源有限的設備（如邊緣設備、IoT 設備、樹莓派等）進行優化。K3s 是輕量級的 Kubernetes 發行版，專注於簡化安裝和運行，特別適合嵌入式和開發環境。

## 安裝和運行

1. K8S: 安裝和配置較為複雜，需要安裝多個組件（如 etcd、kube-apiserver、kube-controller-manager、kube-scheduler 等）。適合有專業運維團隊的環境。

2. K3s: 提供單一二進制文件，內置所有必要的 Kubernetes 元件，簡化了安裝和運行過程。預設使用 SQLite 作為數據庫，可以輕鬆切換到 MySQL 或 PostgreSQL。

## 資源需求

1. K8S: 需要較高的資源（CPU、內存、存儲）來運行所有組件，適合運行在高性能的服務器上。

2. K3s: 減少了不必要的組件和功能，降低了資源需求。適合運行在資源有限的設備上，例如單板計算機、微型服務器等。

## 組件和功能

1. K8S: 包含所有 Kubernetes 的標準組件和功能，包括完整的 API 支持、擴展性功能、存儲管理、網路插件等。

2. K3s: 去除了部分不常用的功能和組件，預設啟用一些輕量級替代方案，例如內置的 SQLite、內置的 Traefik 作為 Ingress 控制器。還有自動啟用的 lightweight 版本的 Containerd 作為預設容器運行時。

## 運行環境

1. K8S: 適合在大型集群和雲環境中運行，需要可靠的網路連接和豐富的硬件資源。

2. K3s: 適合在邊緣環境和嵌入式設備上運行，對網路和硬件資源要求較低，可以在不穩定的網路環境中運行。

## 社區支持和生態系統

1. K8S: 擁有龐大的社區和生態系統，廣泛的支持和豐富的第三方工具和插件。

2. K3s: 社區較小，但由 Rancher Labs 積極維護，並且快速響應輕量級和邊緣應用的需求。

## 其他

1. K8S (Kubernetes): 適合大型、複雜的企業級應用，具有豐富的功能和強大的擴展能力。

2. K3s: 適合資源有限的環境和邊緣設備，簡單、輕量，易於安裝和運行。
