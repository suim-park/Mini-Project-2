# Test main.py

from main import GDP


def test_GDP():
    data_file = "GDP_data.csv"
    result = GDP(data_file)

    max_GDP_rate = max(result.iloc[:, 1])
    assert max_GDP_rate == 3.1


if __name__ == "__main__":
    test_GDP()
