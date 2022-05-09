from app import fonction_retourne_int


def test_index():
    assert "Hello World !" == "Hello World !"


def test_fonction_retourne_int():
    assert type(fonction_retourne_int(10)) == int
    assert fonction_retourne_int("hello world") == "non"
    assert fonction_retourne_int(["hello world"]) == "non"


def toto():
    assert "Hello World !" == "Hello World !"
