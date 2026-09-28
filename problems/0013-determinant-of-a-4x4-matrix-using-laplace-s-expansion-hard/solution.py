
def determinant_4x4(matrix: list[list[int | float]]) -> float:
    # Base case for a 1x1 matrix
    if len(matrix) == 1:
        return float(matrix[0][0])

    # Base case for a 2x2 matrix
    if len(matrix) == 2:
        return float(
            matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        )

    det = 0.0
    # Expand along the first row (row 0)
    for j in range(len(matrix)):
        # Construct the submatrix (minor) by removing the 0th row and jth column
        submatrix = [
            [matrix[i][k] for k in range(len(matrix)) if k != j]
            for i in range(1, len(matrix))
        ]

        # Apply Laplace expansion: determinant += (-1)^j * element * det(submatrix)
        cofactor_sign = 1 if j % 2 == 0 else -1
        det += cofactor_sign * matrix[0][j] * determinant_4x4(submatrix)

    return float(det)