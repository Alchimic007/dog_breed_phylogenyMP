# Phylogenetic Analysis of Dog Breeds

## Overview

Phylogenetic Analysis of Dog Breeds is a project that performs phylogenetic analysis on DNA sequences of various dog breeds to explore their evolutionary relationships. The analysis involves aligning DNA sequences, constructing a phylogenetic tree, and visualizing the tree to understand the genetic closeness between different breeds.

## Features

### Processing FASTA Files

The project provides functions to parse and process FASTA files containing DNA sequences of dog breeds.

### Alignment

It aligns DNA sequences using the Multiple Sequence Alignment technique to identify similarities and differences between sequences.

### Distance Matrix Calculation

Calculates a distance matrix based on the aligned sequences, representing the evolutionary distances between pairs of sequences.

### Phylogenetic Tree Construction

Constructs a phylogenetic tree using the Neighbor-Joining method, which visualizes the evolutionary relationships between dog breeds.

### Visualization

Visualizes the constructed phylogenetic tree to provide insights into the genetic closeness of different breeds.

### Statistical Analysis

Conducts statistical analysis, including Mann-Whitney U tests, to assess the significance of genetic distances between breeds.

### File Structure

├── src/
│   ├── functions/
│   │   ├── process_fasta.py
│   │   ├── distance_matrix.py
│   │   ├── phylogenetic_tree.py
│   │   ├── update_tree_names.py
│   │   ├── write_tree_to_file.py
│   │   ├── calculate_p_values.py
│   │   ├── visualize_phylogenetic_tree.py
│   │   └── __init__.py
│   │
│   ├── classes/
│   │   ├── clade_with_accession.py
│   │   └── __init__.py
│   │
│   └── test/
│       ├── test_master_script.py
│       ├── test_functions.py
│       └── __init__.py
│
├── data/
│   ├── dog_breeds.fa
│   └── mystery.fa
│
└── results/

## Installation

To install the required dependencies, use pip:

``bash
pip install -r requirements.txt

## Usage

### Main Phylogeny Script

To run the main script for performing phylogenetic analysis on real input FASTA files, follow these steps:

1. Ensure you have Python of version not less than 3.11 installed on your system.
2. Clone the repository to your local machine.
3. Run the phylogeny_main.py file with the following command:

``bash
python phylogeny_main.py <input_fasta_file> <unknown_breed_fasta_file>

### Testing
Although main script includes some check I reccommend runnung some tests to check functions consistency

To run the tests, execute the following command:

``bash
python -m unittest discover -s src/tests -p "test_*.py

Also, you can just run testing master script, with following command:

``bash
python phylogeny_test.py

### Contributors
Maxim P. - Project Lead




