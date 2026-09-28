

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.

    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]

    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a, b = matrix[0]
    c, d = matrix[1]

    # Calculate the determinant (ad - bc)
    det = a * d - b * c

    # If determinant is zero, the matrix is singular and not invertible
    if det == 0:
        return None

    # Inverse formula: (1 / det) * [[d, -b], [-c, a]]
    return [[d / det, -b / det], [-c / det, a / det]]

