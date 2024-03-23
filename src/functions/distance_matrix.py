"""
Contains functions for creating a distance matrix.
"""

def create_distance_matrix(alignment):
    """
    Create a distance matrix based on the alignment.

    Args:
        alignment (MultipleSeqAlignment): Multiple sequence alignment object.

    Returns:
        ndarray: Distance matrix.
    """

    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)

    return distance_matrix