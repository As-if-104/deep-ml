def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float] | int:
    # Check if the matrix is empty or if dimensions are incompatible
    if not a or len(a[0]) != len(b):
        return -1

    c = []
    for row in a:
        row_sum = 0
        for i in range(len(b)):
            row_sum += row[i] * b[i]
        c.append(row_sum)

    return c