def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    tp = sum(1 for true, pred in zip(y_true, y_pred) if true == pred) #calculate the tp
    error = len(y_true)-tp #calculate the error

    fp = error
    fn = error

    f1_m = 2*tp/(2*tp+fp+fn)
    return f1_m
    pass