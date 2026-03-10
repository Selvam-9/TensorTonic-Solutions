import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    preds = np.array(predictions)
    num_samples = preds.shape[1]
    final_output = []

    for i in range(num_samples):

        sample_votes = preds[:, i]
        
        counts = np.bincount(sample_votes)
        
        max_votes = np.max(counts)
        winners = np.where(counts == max_votes)[0]
        final_output.append(int(min(winners)))
        
    return final_output
