"""
Contains a custom class for Clade with accession.
"""

import Bio.Phylo.BaseTree

class CladeWithAccession(Bio.Phylo.BaseTree.Clade):
    """
    Custom class for Clade with accession.
    
    Attributes:
        name (str): Name of the clade.
        accession (str): Accession number.
        branch_length (float): Branch length.
        confidence (float): Confidence value.
    """
    def __init__(self, name=None, accession=None, branch_length=None, confidence=None):
        super().__init__(name, branch_length, confidence)
        self.accession = accession

    def __getattr__(self, name):
        if name == 'accession':
            return None
        else:
            return super().__getattr__(name)