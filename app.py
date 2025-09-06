from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def skill():
    message = " Hi {name}! this is a simple Gitlab project"
    return message.format(name=os.getenv("NAME", "Sawsan Salah"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001)