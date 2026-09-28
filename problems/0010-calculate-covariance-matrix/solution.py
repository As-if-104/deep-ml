def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    num_features = len(vectors)
    n = len(vectors[0])

    # Calculate the mean for each feature (row)
    means = [sum(feature) / n for feature in vectors]

    # Initialize the covariance matrix
    cov_matrix = [[0.0] * num_features for _ in range(num_features)]

    # Compute sample covariance between feature i and feature j using (n - 1) degrees of freedom
    for i in range(num_features):
        for j in range(num_features):
            cov = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n)) / (n - 1)
            cov_matrix[i][j] = cov

    return cov_matrix