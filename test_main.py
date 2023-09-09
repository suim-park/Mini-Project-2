# Test main.py

from main import GDP


def test_GDP():
    data_file = "GDP_data.csv"
    result = GDP(data_file)
    assert GDP.loc[0, "GDP rate"] == 2.8


if __name__ == "__main__":
    test_GDP()
