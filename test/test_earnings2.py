import yfinance as yf
import pandas as pd
import time


def get_upcoming_earnings(symbols):
    """
    Fetch upcoming earnings dates using yf.Tickers to reduce API calls.
    """
    earnings_dates = []

    tickers = yf.Tickers(" ".join(symbols))  # Fetch all at once

    for symbol in symbols:
        try:
            stock = tickers.tickers.get(symbol)  # Get stock object
            if stock:
                next_earnings = stock.calendar

                if next_earnings is not None and "Earnings Date" in next_earnings:
                    earnings_date = next_earnings["Earnings Date"]

                    # Handle both single date and date range cases
                    if isinstance(earnings_date, pd.DatetimeIndex):
                        earnings_date = earnings_date[0]

                    earnings_dates.append(
                        {"Symbol": symbol, "Earnings Date": earnings_date}
                    )

                else:
                    print(f"Not found for {symbol}")

            time.sleep(2)  # Increase delay to prevent rate limits

        except Exception as e:
            print(f"Error processing {symbol}: {str(e)}")

    return (
        pd.DataFrame(earnings_dates)
        if earnings_dates
        else pd.DataFrame(columns=["Symbol", "Earnings Date"])
    )


# Example usage
symbols = ["ACN", "FDX", "NKE", "JPM"]
earnings_calendar = get_upcoming_earnings(symbols)
print(earnings_calendar)
