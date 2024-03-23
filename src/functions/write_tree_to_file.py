"""
Contains functions for writing a phylogenetic tree to a file.
"""

def write_tree_to_file(phylogenetic_tree, output_dir, input_fasta):
    """
    Write a phylogenetic tree to a Newick format file.

    Args:
        phylogenetic_tree (Phylo.BaseTree.Tree): Phylogenetic tree object.
        output_dir (str): Output directory.
        input_fasta (str): Input FASTA file path.

    Returns:
        str: Path to the output tree file.
    """
    
    filename_without_extension = os.path.splitext(os.path.basename(input_fasta))[0]
    output_tree_file = os.path.join(output_dir, f"{filename_without_extension}_phylogenetic_tree.newick")
    Phylo.write(phylogenetic_tree, output_tree_file, 'newick')
    
    print(f"Phylogenetic tree saved to: {output_tree_file}")

    return output_tree_file