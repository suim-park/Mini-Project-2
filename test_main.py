# Test main.py

from main import DataShow

GDP_data = {
    "year": [2021, 2022, 2023],
    "GDP rate": [2.8, 3.1, 3.0],
    "GDP": ["1.637M", "1.73M", "1.83M"],
}


def test_DataShow():
    result = DataShow(GDP_data)
    assert result.loc[0, "GDP rate"] == 2.8


if __name__ == "__main__":
    test_DataShow()
