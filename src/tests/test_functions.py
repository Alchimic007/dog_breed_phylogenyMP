import unittest
from functions.process_fasta import process_fasta
from functions.distance_matrix import create_distance_matrix
from functions.phylogenetic_tree import construct_phylogenetic_tree
from functions.update_tree_names import update_tree_names
from functions.write_tree_to_file import write_tree_to_file
from functions.calculate_p_values import calculate_p_values
from functions.visualize_phylogenetic_tree import visualize_phylogenetic_tree


class TestProcessFasta(unittest.TestCase):
    def test_process_fasta(self):
        # Provide sample input files for testing
        input_fasta_file = 'data/dog_breeds.fa'
        unknown_breed_file = 'data/mystery.fa'
        output_dir = 'tests/results'  # Correct output directory path
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
        # Provide sample input alignment for testing
        alignment = [
            ['ACGT', 'ACGT'],
            ['ACGT', 'ACTT']
        ]

        # Call the function with test input
        distance_matrix = create_distance_matrix(alignment)

        # Assert expected outputs
        self.assertIsNotNone(distance_matrix)
        # You can add more assertions based on expected behavior


class TestPhylogeneticTree(unittest.TestCase):
    def test_construct_phylogenetic_tree(self):
        # Provide sample distance matrix for testing
        distance_matrix = [
            [0, 0.2, 0.4],
            [0.2, 0, 0.5],
            [0.4, 0.5, 0]
        ]

        # Call the function with test input
        phylogenetic_tree = construct_phylogenetic_tree(distance_matrix)

        # Assert expected outputs
        self.assertIsNotNone(phylogenetic_tree)
        # You can add more assertions based on expected behavior


class TestUpdateTreeNames(unittest.TestCase):
    def test_update_tree_names(self):
        # Create a sample phylogenetic tree
        class Clade:
            def __init__(self, name=None, accession=None):
                self.name = name
                self.accession = accession

        tree = Clade(name="A", accession="123")
        tree.clades = [Clade(name="B", accession="456")]

        # Define sample breed names and accession numbers
        breed_names = ["Labrador", "German Shepherd"]
        accession_numbers = ["123", "456"]

        # Call the function with test input
        update_tree_names(tree, breed_names, accession_numbers)

        # Assert expected outputs
        self.assertEqual(tree.name, "Labrador")
        self.assertEqual(tree.clades[0].name, "German Shepherd")


class TestWriteTreeToFile(unittest.TestCase):
    def test_write_tree_to_file(self):
        # Provide sample phylogenetic tree for testing
        class PhylogeneticTree:
            def __str__(self):
                return "Sample phylogenetic tree"

        # Create a sample output directory
        output_dir = "output/"

        # Call the function with test input
        output_tree_file = write_tree_to_file(PhylogeneticTree(), output_dir, "input.fasta")

        # Assert expected outputs
        self.assertTrue(output_tree_file.endswith(".newick"))
        # You can add more assertions based on expected behavior


class TestCalculatePValues(unittest.TestCase):
    def test_calculate_p_values(self):
        # Provide sample distance matrix and unknown distances for testing
        distance_matrix = [
            [0, 0.2, 0.4],
            [0.2, 0, 0.5],
            [0.4, 0.5, 0]
        ]
        distances_to_unknown = {"Breed1": 0.2, "Breed2": 0.4}

        # Call the function with test input
        p_values = calculate_p_values(distances_to_unknown, distance_matrix)

        # Assert expected outputs
        self.assertIsNotNone(p_values)
        # You can add more assertions based on expected behavior


class TestVisualizePhylogeneticTree(unittest.TestCase):
    def test_visualize_phylogenetic_tree(self):
        # Provide sample Newick file for testing
        newick_file = "sample_tree.newick"

        # Call the function with test input
        visualize_phylogenetic_tree(newick_file)


if __name__ == '__main__':
    unittest.main()
