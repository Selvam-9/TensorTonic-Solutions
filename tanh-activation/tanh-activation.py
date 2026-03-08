import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    t = np.array(x)
    return ((np.exp(t)-np.exp(-t))/(np.exp(t)+np.exp(-t)))
    # Write code here
    pass