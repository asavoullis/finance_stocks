import yfinance as yf
from datetime import datetime
import pandas as pd
import time  # Import the time module

"""
Verify:

https://www.sectorspdrs.com/earningscalendar
https://www.nasdaq.com/market-activity/earnings
"""


def get_upcoming_earnings(symbols):
    """
    Get upcoming earnings dates for a list of company symbols

    Args:
        symbols (list): List of stock symbols (e.g., ['AAPL', 'MSFT', 'GOOGL'])

    Returns:
        DataFrame: Sorted earnings calendar with company symbols and dates
    """
    earnings_dates = []

    for symbol in symbols:
        try:
            # Get stock info
            stock = yf.Ticker(symbol)

            # Get next earnings date
            next_earnings = stock.calendar

            if next_earnings is not None and "Earnings Date" in next_earnings:
                earnings_date = next_earnings["Earnings Date"]

                # Handle both single date and date range cases
                if isinstance(earnings_date, pd.DatetimeIndex):
                    earnings_date = earnings_date[0]

                earnings_dates.append(
                    {
                        "Symbol": symbol,
                        "Earnings Date": earnings_date,
                    }
                )
                # print(f"Found earnings date for {symbol}: {earnings_date}")
            else:
                print(f"Not found for {symbol}")

            time.sleep(1)  # Add a 1-second delay between each request

        except Exception as e:
            print(f"Error processing {symbol}: {str(e)}")

    # Create DataFrame and sort by date
    if earnings_dates:
        df = pd.DataFrame(earnings_dates)
        df = df.sort_values("Earnings Date")

        # print(df.dtypes)
        # print(df.head))

        # Extract the first date from the list and format it as 'dd-mm-yyyy'
        df["Date"] = df["Earnings Date"].apply(
            lambda x: (
                x[0].strftime("%d-%m-%Y")
                if isinstance(x, list)
                else x.strftime("%d-%m-%Y")
            )
        )

        return df
    else:
        return pd.DataFrame(columns=["Symbol", "Earnings Date"])


if __name__ == "__main__":
    # Example usage
    symbols = stocks = [
        # "CRM",
        # "ASML",
        # "INTC",
        # "BBAI",
        # "SMCI",
        # "NVDA",
        # "PLTR",
        # "AAPL",
        # "MSFT",
        # "GOOGL",
        # "AMZN",
        # "META",
        # "ORCL",  # oracle
        # "ADBE",  # adobe
        "ACN",  # accentre
        "FDX",  # FedEx
        "NKE",  # Nike
        "JPM",  # JPMorgan Chase
    ]

    print("Fetching upcoming earnings dates...")
    earnings_calendar = get_upcoming_earnings(symbols)

    if not earnings_calendar.empty:
        print("\nUpcoming Earnings Calendar:")
        print(earnings_calendar)
        print(earnings_calendar.dtypes)

        # print(earnings_calendar.to_string(index=False))
    else:
        print("\nNo earnings dates found.")
