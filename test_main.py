# Test main.py

from main import GDP

GDP_data = {
    "year": [2021, 2022, 2023],
    "GDP rate": [2.8, 3.1, 3.0],
    "GDP": ["1.637M", "1.73M", "1.83M"],
}


def test_GDP():
    result = GDP(GDP_data)

    max_GDP_rate = max(result.iloc[:, 1])
    assert max_GDP_rate == 3.1


if __name__ == "__main__":
    test_GDP()
