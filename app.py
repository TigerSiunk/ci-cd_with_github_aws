from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World !"


@application.route("/attaque")
def attaque():
    return "Attaque effectuée"


def fonction_retourne_int(integer):
    if type(integer) == int:
        return 10
    return "non"

if __name__ == "__main__":
    application.run()
