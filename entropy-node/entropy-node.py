import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    if y==0 or len(y) == 0:
        return 0.0
    else:
        unique_class,counts = np.unique(y,return_counts=True)
        probabilities = counts/len(y)
        entropy = -np.sum(probabilities*(np.log2(probabilities)))
        return entropy
    pass