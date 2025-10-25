from src.greek import greek



def test_greeking():

    expected = "Hello, Mohamed"

    result = greek("Mohamed")

    assert result == expected