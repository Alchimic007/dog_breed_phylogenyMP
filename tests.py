from Bio import Phylo
import Bio.Phylo.BaseTree
from Bio.Phylo.TreeConstruction import DistanceMatrix
from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Align import MultipleSeqAlignment
import numpy as np
import pandas as pd
import unittest
import sys
from src.functions import process_fasta, create_distance_matrix, construct_phylogenetic_tree, update_tree_names, write_tree_to_file, calculate_p_values, visualize_phylogenetic_tree, plot_bar_chart_and_histogram 
from src.classes import CladeWithAccession
import tempfile
import os


class TestProcessFasta(unittest.TestCase):
    def test_process_fasta(self):
        # Provide sample input files for testing
        input_fasta_file = 'data/dog_breeds.fa'
        unknown_breed_file = 'data/mystery.fa'
        output_dir = 'src/tests'  
        # Call the function with test input
        alignment1, output_fasta1, results_dir1, breed_names1, accession_numbers1 = process_fasta(input_fasta_file, align=True, output_dir=output_dir)
        alignment2, output_fasta2, results_dir2, breed_names2, accession_numbers2 = process_fasta(unknown_breed_file, align=True, output_dir=output_dir)

        # Assert expected outputs
        self.assertIsNotNone(alignment1)
        self.assertIsNotNone(output_fasta1)
        self.assertIsNotNone(results_dir1)
        self.assertGreater(len(breed_names1), 0)
        self.assertGreater(len(accession_numbers1), 0)

        self.assertIsNotNone(alignment2)
        self.assertIsNotNone(output_fasta2)
        self.assertIsNotNone(results_dir2)
        self.assertGreater(len(breed_names2), 0)
        self.assertGreater(len(accession_numbers2), 0)


class TestDistanceMatrix(unittest.TestCase):
    def test_create_distance_matrix(self):
        # Create a sample input alignment for testing
        seq1 = SeqRecord(Seq('ACGT'), id='Seq1')
        seq2 = SeqRecord(Seq('ACGT'), id='Seq2')
        seq3 = SeqRecord(Seq('ACGT'), id='Seq3')
        seq4 = SeqRecord(Seq('ACTT'), id='Seq4')

        alignment = MultipleSeqAlignment([seq1, seq2, seq3, seq4])

        # Call the function with test input
        distance_matrix = create_distance_matrix(alignment)

        # Assert expected outputs
        self.assertIsNotNone(distance_matrix)
        




class TestPhylogeneticTree(unittest.TestCase):
    def test_construct_phylogenetic_tree(self):
        # Provide sample distance matrix for testing
        distance_matrix = [
            [0, 0.2, 0.4],
            [0.2, 0, 0.5],
            [0.4, 0.5, 0]
        ]

        # Convert the distance matrix to lower triangle format
        lower_triangle_matrix = []
        for i in range(len(distance_matrix)):
            lower_triangle_matrix.append(distance_matrix[i][:i+1])

        # Call the function with test input
        dist_mat = DistanceMatrix(names=['Breed1', 'Breed2', 'Breed3'], matrix=lower_triangle_matrix)

        phylogenetic_tree = construct_phylogenetic_tree(dist_mat)

        # Assert expected outputs
        self.assertIsNotNone(phylogenetic_tree)
        


       

class TestWriteTreeToFile(unittest.TestCase):
    def test_write_tree_to_file(self):
        # Create a sample phylogenetic tree for testing
        phylogenetic_tree = Phylo.BaseTree.Tree()

        # Call the function with test input
        output_dir = "src/tests"
        input_fasta = "input.fasta"
        
        # Pass a list containing the phylogenetic tree to the function
        output_tree_file = write_tree_to_file([phylogenetic_tree], output_dir, input_fasta)

        # Assert expected outputs
        self.assertTrue(output_tree_file.endswith(".newick"))
        self.assertTrue(os.path.exists(output_tree_file))
        


class TestCalculatePValues(unittest.TestCase):
    def test_calculate_p_values(self):
        # Provide sample distance matrix and unknown distances for testing
        distance_matrix = [
            [0, 0.2, 0.4],
            [0.2, 0, 0.5],
            [0.4, 0.5, 0]
        ]
        distances_to_unknown = {"unknown": 0} 

        # Call the function with test input
        p_values = calculate_p_values(distances_to_unknown, distance_matrix)

        # Assert expected outputs
        self.assertIsNotNone(p_values)
        




class TestPlotBarChartAndHistogram(unittest.TestCase):
    def test_plot_bar_chart_and_histogram(self):
        # Provide sample DataFrame for testing
        df_closeness = pd.DataFrame({
            'Breed': ['Breed1', 'Breed2', 'Breed3'],
            'Distance to unknown': [0.1, 0.2, 0.3]
        })

        # Provide sample output directory and filename
        output_dir = 'src/tests'
        filename_without_extension = 'test_output'

        # Call the function with test input
        plot_bar_chart_and_histogram(df_closeness, output_dir, filename_without_extension)

        # Assert expected outputs
        bar_chart_path = os.path.join(output_dir, f"{filename_without_extension}_closeness_distribution_with_names.png")
        histogram_path = os.path.join(output_dir, f"{filename_without_extension}_distance_distribution.png")
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Assert that the files exist
        self.assertTrue(os.path.exists(bar_chart_path))
        self.assertTrue(os.path.exists(histogram_path))


if __name__ == '__main__':
    unittest.main()
