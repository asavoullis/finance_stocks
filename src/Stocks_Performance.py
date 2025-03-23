import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def calculate_price_change(current_price, historical_price):
    """
    Calculate percentage change between current and historical price
    """
    if historical_price == 0:
        return 0
    return ((current_price - historical_price) / historical_price) * 100

def get_stock_performance(ticker_symbols):
    """
    Get comprehensive stock performance for a list of symbols
    
    Args:
        ticker_symbols (list): List of stock ticker symbols (e.g., ['NVDA', 'AAPL'])
    
    Returns:
        pandas.DataFrame: Performance metrics for each stock
    """
    results = []
    
    for symbol in ticker_symbols:
        try:
            # Create ticker object
            stock = yf.Ticker(symbol)
            
            # Get current data
            current_data = stock.info
            current_price = current_data.get('regularMarketPrice', 0)
            
            # Get historical data
            end_date = datetime.now()
            start_date = end_date - timedelta(days=3650)  # 10 years
            hist = stock.history(start=start_date, end=end_date)
            
            # Convert index to naive datetime for consistent comparison
            hist.index = hist.index.tz_localize(None)
            
            # Calculate all the required timeframes
            time_periods = {
                '1d': 1,
                '3d': 3,
                '5d': 5,
                '15d': 15,
                '1m': 30,
                '2m': 60,
                '3m': 90,
                '6m': 180,
                '1y': 365,
                '2y': 730,
                # '3y': 1095,
                # '5y': 1825,
                # '10y': 3650
            }
            
            changes = {'Symbol': symbol, 'Current Price': current_price}
            
            # Calculate YTD change
            ytd_start = datetime(end_date.year, 1, 1)
            ytd_data = hist[hist.index >= ytd_start]
            if not ytd_data.empty:
                ytd_change = calculate_price_change(current_price, ytd_data.iloc[0]['Close'])
                changes['YTD'] = f"{ytd_change:.2f}%"
            
            # Calculate changes for all periods
            for period_name, days in time_periods.items():
                try:
                    historical_data = hist[hist.index <= (end_date - timedelta(days=days))]
                    if not historical_data.empty:
                        historical_price = historical_data.iloc[-1]['Close']
                        change = calculate_price_change(current_price, historical_price)
                        changes[period_name] = f"{change:.2f}%"
                    else:
                        changes[period_name] = "N/A"
                except Exception:
                    changes[period_name] = "N/A"
            
            results.append(changes)
            
        except Exception as e:
            print(f"Error processing {symbol}: {str(e)}")
            continue
    
    # Create DataFrame from results
    df = pd.DataFrame(results)
    
    # Reorder columns to match requested format
    columns = ['Symbol', 'Current Price', '1d', '3d', '5d', '15d', '1m', '2m', '3m', 
              '6m', 'YTD', '1y', '2y']
    df = df[columns]
    
    return df

# Example usage:
if __name__ == "__main__":
    # Example stock list
    stocks = ['CRM', 'ASML','INTC' , 'BBAI', 'SMCI', 'NVDA', 'PLTR', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
    
    # Get performance data
    performance_df = get_stock_performance(stocks)
    
    # Display results
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print("\nStock Performance Summary:")
    print(performance_df)

