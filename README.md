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

## Usage

### Main Master Script

To run the main script for performing phylogenetic analysis on real input FASTA files, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the src directory.
4. Run the main_master_script.py file with the following command:

```bash
python main_master_script.py <input_fasta_file> <unknown_breed_file>


