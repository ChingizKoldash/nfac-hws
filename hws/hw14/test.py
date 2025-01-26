from main import extract

def test_extract():
    assert extract(3, 2) == 1
    assert extract(1, -1) == 2
    assert extract(0, 0) == 0
