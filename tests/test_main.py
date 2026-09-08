from src.main import main

def test_main():
    result = main()
    assert result == "Booking Platform"
def test_main_returns_string():
    result = main()
    assert isinstance(result, str)