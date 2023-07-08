import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

def generate_payoff_independent(price_range, range_day, options, stock_price):
  '''
  Generates a simple payoff when  provided with a list of options
  
  input params
  price_range(df): a dataframe with max and min values of price that can be reached in a specific 
                    range of days you want to plot with
  range_day(int): Number of days corresponding to which the price range needs to be used
  options(list): A list of dictionaries providing the specs of the options
  stock_price(float): Current stock price
    
  '''

    payoff_data = pd.DataFrame(columns=['Stock Price', 'Payoff'])
    stock_price_range = np.linspace(
        float(price_range[price_range['Days'] == range_day].iloc[0, 1]),
        float(price_range[price_range['Days'] == range_day].iloc[0, 2]),
        100
    )
    
    for x in stock_price_range:
        payoff= option_combination_payoff(x, options)

        #print(x,payoff)
        payoff_data = pd.concat([payoff_data, pd.DataFrame([[x, payoff]], columns=['Stock Price', 'Payoff'])])
    
    plt.figure(figsize=(10,6))
    plt.plot(payoff_data['Stock Price'], payoff_data['Payoff'])
    plt.axhline(y=0, color='y', linestyle='-', linewidth=1)
    strike_prices=[]
    for option in options:
        strike_prices.append(option['strike_price'])
    #print(list(set(strike_prices)))
        
    for strike_price in list(set(strike_prices)):
        plt.axvline(x=strike_price,color='b', linestyle='-', label='Strike Price')

    #plt.axvline(x=break_even,color='r', linestyle='-', label='Breakeven')
        
    plt.axvline(x=stock_price, color='g', linestyle='--', label='Stock Price')
    #ax.text(break_even, np.min(payoff_data['Payoff']), f" {breakeven}", ha='right', va='top', color='r')
    plt.xlabel('Stock Price')
    plt.ylabel('Payoff')
    plt.title('Option Combination Payoff')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#Calling the function
my_opts=[
    {'option_type':'call',
     'strike_price':19000,
     'premium':490.2,
     'lots':1,
     'lot_size':50,
     'position':'short'},
    
    {'option_type':'put',
     'strike_price':19500,
     'premium':248,
     'lots':1,
     'lot_size':50,
     'position':'short'},
    
#     {'option_type':'call',
#      'strike_price':18800,
#      'premium':280,
#      'lots':3,
#      'lot_size':50,
#      'position':'long'},
    
#     {'option_type':'put',
#      'strike_price':18700,
#      'premium':248,
#      'lots':3,
#      'lot_size':50,
#      'position':'long'}
 ]
generate_payoff_independent(price_range, 7, my_opts, current_price)
