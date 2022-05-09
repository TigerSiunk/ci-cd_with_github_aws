from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World !"


@app.route("/attaque")
def attaque():
    return "Attaque effectuée"


if __name__ == "__main__":
    app.run()
