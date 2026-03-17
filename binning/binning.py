def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    min_value = min(values)    
    max_value = max(values)
    bin_with = (max_value-min_value)/num_bins
    indices=[]
    if min_value==max_value:
        return [0]*len(values)
    else:
        for x in values:
            idx = int((x - min_value) / bin_with)
            if idx == num_bins: 
                idx = num_bins - 1
            indices.append(idx)
        return indices
    