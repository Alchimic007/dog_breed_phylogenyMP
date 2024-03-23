"""
Contains functions for visualizing a phylogenetic tree.
"""

def visualize_phylogenetic_tree(newick_file):
    """
    Visualize a phylogenetic tree and save the visualization as an image.

    Args:
        newick_file (str): Path to the Newick format file.
    """
    
    tree = Phylo.read(newick_file, 'newick')
    node_colors = {}
    for clade in tree.find_clades():
        if clade.name == "unknown":
            node_colors[clade] = 'red'
        else:
            node_colors[clade] = 'black'

    plt.figure(figsize=(30, 40))
    Phylo.draw(tree, axes=plt.gca(), label_func=lambda x: x.name if x.name == "unknown" or x.is_terminal() else '', label_colors=node_colors, show_confidence=False, do_show=False)

    for line in plt.gca().get_lines():
        line.set_linewidth(2)

    plt.axis('off')

    output_image_file = os.path.join(os.path.dirname(newick_file), 'phylogenetic_tree_visualization.png')
    plt.savefig(output_image_file, bbox_inches='tight', pad_inches=0.2)
    plt.show()