from flask import Flask

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def index():
    return {
        "channel": "Hello, World!",
        "tutorial":"React, Flask & Docker"
    }

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")