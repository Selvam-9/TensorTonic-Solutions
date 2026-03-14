def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    DO NOT SORT the series; time order must be preserved.
    """
    current_data = list(series) 
    
    for _ in range(order):
        new_diffs = []
        # Calculate x[t] - x[t-1] based on current order
        for i in range(1, len(current_data)):
            new_diffs.append(current_data[i] - current_data[i-1])
        current_data = new_diffs
        
        if not current_data:
            break
            
    return current_data

