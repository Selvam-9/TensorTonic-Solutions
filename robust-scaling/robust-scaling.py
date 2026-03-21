def get_median(data):
    n = len(data)
    if n == 0: return 0
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]

def robust_scaling(values):
    if not values:
        return []
        
    s = sorted(values)
    n = len(s)
    
    # 1. Calculate Median
    median = get_median(s)
    
    # 2. Determine halves for Q1 and Q3
    mid = n // 2
    if n % 2 == 0:
        lower_half = s[:mid]
        upper_half = s[mid:]
    else:
        # For odd lengths, exclude the actual median from both halves
        lower_half = s[:mid]
        upper_half = s[mid + 1:]
    
    # 3. Calculate Q1 and Q3
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    iqr = q3 - q1
    
    result = []
    for x in values: # Use original 'values' to maintain input order
        if iqr == 0:
            result.append(x - median)
        else:
            result.append((x - median) / iqr)
            
    return result
        
        