#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.
    """
    n = len(matrix)
    for layer in range(n // 2):
        offset = 0
        last = n - 1 - layer
        for i in range(layer, last):
            # Save top
            top = matrix[layer][i]
            # Left -> Top
            matrix[layer][i] = matrix[last - offset][layer]
            # Bottom -> Left
            matrix[last - offset][layer] = matrix[last][last - offset]
            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]
            # Top -> Right
            matrix[i][last] = top
            offset += 1
