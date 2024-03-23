"""
Contains functions for calculating p-values.
"""

def calculate_p_values(distances_to_unknown, distance_matrix):
    """
    Calculate p-values for distances to unknown breeds.

    Args:
        distances_to_unknown (dict): Distances to unknown breeds.
        distance_matrix (ndarray): Distance matrix.

    Returns:
        dict: P-values.
    """
    p_values = {}
    unknown_breed_index = distances_to_unknown['unknown']
    for i, breed in enumerate(distances_to_unknown):
        if breed != 'unknown':
            _, p_value = mannwhitneyu(distance_matrix[unknown_breed_index], distance_matrix[i], alternative='two-sided')
            p_values[breed] = p_value
    return p_values