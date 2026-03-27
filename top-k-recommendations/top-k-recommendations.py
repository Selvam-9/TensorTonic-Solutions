def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
        # 1. Filter and pair (score, index)
    candidates = [(scores[i], i) for i in range(len(scores)) if i not in rated_indices]
    
    # 2. Sort by score descending
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    # 3. Return top k indices
    return [index for score, index in candidates[:k]]