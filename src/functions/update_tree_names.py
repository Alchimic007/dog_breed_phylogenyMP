"""
Contains functions for updating tree names.
"""

def update_tree_names(tree, breed_names, accession_numbers):
    """
    Update the names of clades in a phylogenetic tree.

    Args:
        tree (Phylo.BaseTree.Tree): Phylogenetic tree object.
        breed_names (list): List of breed names.
        accession_numbers (list): List of accession numbers.
    """
   
    for clade in tree.find_clades(terminal=True):
        if clade.name and '|' in clade.name:
            accession_id = clade.name.split('|')[1]
            match = re.search(r'\w+', accession_id)
            if match:
                accession_part = match.group()
                breed_index = (int(accession_part, 36) - 1) % len(accession_numbers)
                updated_name = f"{breed_names[breed_index]}_{accession_numbers[breed_index]}"
                updated_name = updated_name.replace("Mixed_breed_", "Mixed_")
                clade.name = updated_name

