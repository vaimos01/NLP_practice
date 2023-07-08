import yfinance as yf
import numpy as np
import pandas as pd
import math
from prettytable import PrettyTable

#Download data from yfin and calculate daily stock returns
def download_stock_data(ticker, start_date, end_date):
    # Download the stock price data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_stock_returns(stock_data):
    # Calculate the stock returns
    stock_returns = stock_data['Adj Close'].pct_change()
    return stock_returns

def get_dates():
    today = datetime.date.today()+datetime.timedelta(days=1)
    one_year_ago = today - datetime.timedelta(days=365)
    return today, one_year_ago

#Generate business days
def is_weekend(date):
    return date.weekday() >= 5  # Saturday = 5, Sunday = 6

def is_indian_holiday(date):
    # Add your Indian government holiday dates here
    # Example: January 1, 2023
    holiday_dates = [
        datetime.date(2023, 1, 1),
        # Add more holiday dates here
    ]
    return date in holiday_dates

def business_days_between(start_date, end_date):
    business_days = np.busday_count(start_date, end_date)
    current_date = start_date
    while current_date <= end_date:
        if is_weekend(current_date) or is_indian_holiday(current_date):
            business_days -= 1
        current_date += datetime.timedelta(days=1)
    return business_days


def get_volatility(stock_data, days):
    # Calculate the daily returns
    daily_returns = stock_data['Close'].pct_change()

    # Calculate the annualized volatility using the daily returns
    volatility = daily_returns.std() * np.sqrt(days)
    return volatility


def generate_price_range_table(stock_data):
    # Define the list of standard time windows in days
    days_list = [7, 14, 30, 60, 90, 180]

    # Define the table headers
    headers = ['Days', 'Low','High']

    # Initialize the table rows
    rows = []

    # Loop over the list of days and generate the price range for each day
    for days in days_list:
        volatility = get_volatility(stock_data, days)
        current_price = stock_data['Close'].iloc[-1]
        low_price = current_price - 2 * current_price * volatility
        high_price = current_price + 2 * current_price * volatility
        #price_range = f'{low_price:.2f} - {high_price:.2f}'

        # Add the row to the table
        rows.append([days, f'{low_price:.2f}',f'{high_price:.2f}'])

    # Print the table using PrettyTable
    #print (rows)
    table = pd.DataFrame(columns=headers,data=rows)#.set_index('Days')
    #print (table)
    

    #print(table)
    return table

def generate_summ(ticker):
    today,one_year_ago=get_dates()
    num_bus_day=business_days_between(one_year_ago, today)
    stock_data=download_stock_data(ticker,one_year_ago,today)
    current_price = stock_data['Close'].iloc[-1]
    sigma=get_volatility(stock_data, days=365)
    price_range=generate_price_range_table(stock_data)
    return today,one_year_ago, num_bus_day,stock_data,sigma,price_range,current_price



def vix(ind_ticker,us_ticker):
    today,one_year_ago=get_dates()
    ind_vix=download_stock_data(ind_ticker,one_year_ago,today)
    ind_current_price = ind_vix['Close'].iloc[-1]
    us_vix=download_stock_data(us_ticker,one_year_ago,today)
    us_current_price = us_vix['Close'].iloc[-1]
    print(f'India VIX:{ind_current_price} \nUS VIX: {us_current_price}')
    price_range=generate_price_range_table(us_vix)
    return price_range
