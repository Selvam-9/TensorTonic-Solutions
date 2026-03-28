def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    dim = len(points[0]) if points else 0
    centroids = []

    for i in range(k):
        # Filter points belonging to the current cluster
        cluster_points = [p for p, a in zip(points, assignments) if a == i]
        
        if not cluster_points:
            centroids.append([0.0] * dim)
        else:
            # Average each dimension
            mean = [sum(dim_vals) / len(cluster_points) for dim_vals in zip(*cluster_points)]
            centroids.append(mean)
            
    return centroids