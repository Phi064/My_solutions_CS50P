from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("4/4") == 100
    assert convert("2/4") == 50
    assert convert("0/4") == 0
    with pytest.raises(Exception):
        convert("5/4")
    
def test_gauge():
    assert gauge(100) == "F"
    assert gauge(50) == f"{50}%"
    assert gauge(75) == f"{75}%"
    assert gauge(0) == "E"