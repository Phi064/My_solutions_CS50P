from bank import value

def test_hello():
    assert value("Hello") == 0

def test_h():
    assert value("Hi") == 20
    assert value("How are you") == 20
    assert value("Hey") == 20

def test_not_h():
    assert value("Welcome") == 100
    assert value("This is the bank") == 100