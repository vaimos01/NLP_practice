#get appropriate lot numbers based on delta neutralizing

def calculate_num_lots(call_deltas, put_deltas, delta_tolerance, strategy):
    call_num_lots = [1 / delta for delta in call_deltas]
    put_num_lots = [-1 / delta for delta in put_deltas]
    delta_difference = sum(call_deltas) + sum(put_deltas)
    

    if delta_difference <= delta_tolerance:
        return call_num_lots, put_num_lots,delta_difference
    else:
        delta_adjustment = delta_tolerance / delta_difference
        call_num_lots = [lot_size * delta_adjustment for lot_size in call_num_lots]
        put_num_lots = [lot_size * delta_adjustment for lot_size in put_num_lots]

        if strategy == 'long_straddle' or strategy == 'short_straddle':
            call_num_lots = [lot_size * 0.5 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.5 for lot_size in put_num_lots]
        elif strategy == 'long_strangle' or strategy == 'short_strangle':
            call_num_lots = [lot_size * 0.5 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.5 for lot_size in put_num_lots]
        elif strategy == 'bull_call_spread' or strategy == 'bear_call_spread':
            call_num_lots = [lot_size * 0.7 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.3 for lot_size in put_num_lots]
        elif strategy == 'bear_put_spread' or strategy == 'bull_put_spread':
            call_num_lots = [lot_size * 0.3 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.7 for lot_size in put_num_lots]
        elif strategy == 'long_call_butterfly' or strategy == 'short_call_butterfly':
            call_num_lots = [lot_size * 0.25 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.25 for lot_size in put_num_lots]
            return call_num_lots + [-2 * lot_size for lot_size in call_num_lots] + call_num_lots, put_num_lots
        elif strategy == 'long_put_butterfly' or strategy == 'short_put_butterfly':
            call_num_lots = [lot_size * 0.25 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.25 for lot_size in put_num_lots]
            return call_num_lots, put_num_lots + [-2 * lot_size for lot_size in put_num_lots] + put_num_lots
        elif strategy == 'long_call_condor' or strategy == 'short_call_condor':
            call_num_lots = [lot_size * 0.4 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.4 for lot_size in put_num_lots]
            return call_num_lots + [-lot_size for lot_size in call_num_lots] + call_num_lots + [-lot_size for lot_size in call_lot_sizes], put_num_lots
        elif strategy == 'long_put_condor' or strategy == 'short_put_condor':
            call_num_lots = [lot_size * 0.4 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.4 for lot_size in put_num_lots]
            return call_num_lots, put_num_lots + [-lot_size for lot_size in put_num_lots] + put_num_lots + [-lot_size for lot_size in put_num_lots]
        elif strategy == 'protective_collar':
            call_num_lots = [lot_size * 0.8 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.8 for lot_size in put_num_lots]
        elif strategy == 'iron_condor':
            call_num_lots = [lot_size * 0.5 for lot_size in call_num_lots]
            put_num_lots = [lot_size * 0.5 for lot_size in put_num_lots]

        return call_num_lots, put_num_lots,delta_difference
