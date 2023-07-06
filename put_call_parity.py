def cumulative_normal_distribution(x):
  '''
  Returns probability value per normal distribution
  '''
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def black_scholes(S, K, r, sigma, T):
  '''
  Generate theoretical call and put price
  '''
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    N_d1 = cumulative_normal_distribution(d1)
    N_d2 = cumulative_normal_distribution(d2)
    call_price = S * N_d1 - K * math.exp(-r * T) * N_d2
    put_price = K * math.exp(-r * T) * (1 - N_d2) - S * (1 - N_d1)
    return call_price, put_price



def check_put_call_parity(S, K, r, sigma, T, call_price, put_price):
  '''
  Check for put call parity for a specific strike
  '''
    theoretical_call_price, theoretical_put_price = black_scholes(S, K, r, sigma, T)

    # Check if the put-call parity holds
    diff = round(call_price - put_price + K * math.exp(-r * T) - S, 6)
    if diff == 0:
        print("Put-call parity holds")
        print("Theoretical call price:", theoretical_call_price)
        print("Theoretical put price:", theoretical_put_price)
    else:
        print("Put-call parity does not hold")
        print("Difference between LHS and RHS:", diff)

    return theoretical_call_price, theoretical_put_price, diff

