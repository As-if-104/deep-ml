import numpy as np


def reshape_matrix(
    a: list[list[int | float]], new_shape: tuple[int, int]
) -> list[list[int | float]]:
    # Convert list to numpy array
    np_arr = np.array(a)

    # Check if total elements match the required new shape dimensions
    if np_arr.size != new_shape[0] * new_shape[1]:
        return []

    # Reshape and convert back to Python list
    reshaped_matrix = np_arr.reshape(new_shape).tolist()
    return reshaped_matrix