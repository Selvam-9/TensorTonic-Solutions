import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    numerator = np.sum((np.array(y_true)-np.array(y_pred))**2)
    ym = np.mean(y_true)
    denominator = np.sum((y_true-ym)**2)
    
    if denominator==0:
        return 1.0 if numerator==0 else 0.0
    return 1-(numerator/denominator)

    pass