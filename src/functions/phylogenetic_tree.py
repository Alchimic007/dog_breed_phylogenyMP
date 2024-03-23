"""
Contains functions for constructing a phylogenetic tree.
"""

def construct_phylogenetic_tree(distance_matrix):
    """
    Construct a phylogenetic tree from a distance matrix.

    Args:
        distance_matrix (ndarray): Distance matrix.

    Returns:
        Phylo.BaseTree.Tree: Phylogenetic tree object.
    """
    
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(distance_matrix)

    return tree

