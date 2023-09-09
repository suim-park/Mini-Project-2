# Test main.py

from main import GDP


def test_GDP():
    assert GDP.loc[0, "GDP rate"] == 2.8


if __name__ == "__main__":
    test_GDP()
