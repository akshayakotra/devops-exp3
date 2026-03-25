from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Client IP Address:192.168.20.109 <br> URL requested: localhost:flask <br> HTTP status code : 7612 <br> Response time 1.12 sec"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

run this code in terminal using python3 app.py and in firefox type 127.0.0.1/flask
