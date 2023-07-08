#payoff with lot size and number of lots computation

def ind_long_call_payoff(stock_price, strike, premium,lots,lot_size):
    return (max(stock_price - strike,0)-premium)*lot_size*lots

def ind_long_put_payoff(stock_price, strike, premium,lots,lot_size):
    return (max(strike - stock_price,0) -premium)*lot_size*lots

def ind_short_call_payoff(stock_price, strike, premium,lots,lot_size):
    return (min(strike - stock_price,0)+ premium)*lot_size*lots

def ind_short_put_payoff(stock_price, strike, premium,lots,lot_size):
    return (premium - max(strike - stock_price, 0))*lot_size*lots

def option_combination_payoff(stock_price,options):
    
    total_payoff = 0
    #breakeven=stock_price
    #strike_prices=[]
    
    for option in options:
        strike_price = option['strike_price']
        premium = option['premium']
        lot_size = option['lot_size']
        lots = option['lots']
        position = option['position']
        option_type = option['option_type']
        #print(option_type)
        
        if position == 'long':
            if option_type=='call':
                long_call_payoff = ind_long_call_payoff(stock_price, strike_price, premium,lots,lot_size)
                total_payoff=total_payoff+long_call_payoff
            
            elif option_type=='put':
                long_put_payoff = ind_long_put_payoff(stock_price,strike_price, premium,lots,lot_size)
                total_payoff=total_payoff+long_put_payoff
              

        elif position == 'short':
            if option_type=='call':
                short_call_payoff = ind_short_call_payoff(stock_price, strike_price, premium,lots,lot_size)
                total_payoff=total_payoff+short_call_payoff
              
                #print(total_payoff)
            elif option_type=='put':
                short_put_payoff = ind_short_put_payoff(stock_price,strike_price, premium,lots,lot_size)
                total_payoff=total_payoff+short_put_payoff
                
                #print(total_payoff)

        else:
            raise ValueError("Invalid position. Position must be 'long' or 'short' and 'call' or 'put'.")
    
    return total_payoff
