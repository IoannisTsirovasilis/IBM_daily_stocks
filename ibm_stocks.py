import pandas

FILE_PATH = "files/IBM.csv"
OUTPUT_FILE_PATH = "files/results.csv"


def calculate_daily_stock_variance(open_value: float, close_value: float):
    return 100 * (open_value - close_value) / open_value


def main():
    content = pandas.read_csv(FILE_PATH)
    content["Daily Stock"] = 100 * (content["Open"] - content["Close"]) / content["Open"]
    content.to_csv(OUTPUT_FILE_PATH)


if __name__ == "__main__":
    main()
