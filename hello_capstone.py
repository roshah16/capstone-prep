from datetime import date


def main():
    print("Welcome to Capstone Investment Advisors!")
    print(f"Today's date: {date.today():%A, %B %d, %Y}")
    print("\nAsset classes traded at Capstone:")
    for asset_class in ("Rates", "FX", "Volatility Options"):
        print(f"  - {asset_class}")


if __name__ == "__main__":
    main()
