# 資料結構
'''
/myflaskapp 
	/templates 
		index.html 
	/static 
		/css 
			style.css 
	app.py 
	requirements.txt
'''
# index.html
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to My Flask App!</h1>
</body>
</html>
'''
# style.css
'''
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 50px;
}
'''
# requirements.txt
'''
Flask==2.0.1
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)