import sys
from src.functions import process_fasta, create_distance_matrix, construct_phylogenetic_tree, update_tree_names, write_tree_to_file, calculate_p_values, visualize_phylogenetic_tree
from src.classes import CladeWithAccession

def test_master_script():
    input_fasta_file = 'data/dog_breeds.fa'
    unknown_breed_file = 'data/mystery.fa'

    try:
        dog_alignment, dog_output_fasta, dog_output_directory, dog_breed_names, dog_accession_numbers = process_fasta(
            input_fasta_file, align=True)
        if not dog_alignment:
            raise ValueError("Alignment for dog breeds failed or no sequences found.")
        print("Alignment for dog breeds completed successfully.")

        mystery_alignment, mystery_output_fasta, mystery_output_directory, _, mystery_accession_numbers = process_fasta(
            unknown_breed_file, align=True)
        if not mystery_alignment:
            raise ValueError("Alignment for the mystery sequence failed or no sequences found.")
        print("Alignment for the mystery sequence completed successfully.")

        if dog_alignment and mystery_alignment:
            dog_alignment.extend(mystery_alignment)
            dog_accession_numbers.extend(mystery_accession_numbers)
        else:
            raise ValueError("Concatenation failed.")

        distance_matrix = create_distance_matrix(dog_alignment)
        if not distance_matrix:
            raise ValueError("Creating distance matrix failed.")
        print("Distance matrix created successfully.")

        phylogenetic_tree = construct_phylogenetic_tree(distance_matrix)
        if not phylogenetic_tree:
            raise ValueError("Constructing phylogenetic tree failed.")
        print("Phylogenetic tree constructed successfully.")

        dog_breed_names.append("unknown")
        update_tree_names(phylogenetic_tree, dog_breed_names, dog_accession_numbers)

        output_tree_file = write_tree_to_file(phylogenetic_tree, dog_output_directory, input_fasta_file)

        distances_to_unknown = {}
        unknown_breed_index = dog_breed_names.index("unknown")
        for i, breed_name in enumerate(dog_breed_names):
            distance = distance_matrix[unknown_breed_index, i]
            distances_to_unknown[breed_name] = distance

        df_closeness = pd.DataFrame({
            'Breed': [breed for breed in distances_to_unknown.keys() if breed != 'unknown'],
            'Distance to unknown': [distance for breed, distance in distances_to_unknown.items() if breed != 'unknown']
        })

        p_values = calculate_p_values(distances_to_unknown, distance_matrix)

        df_closeness['p-values'] = [p_values.get(breed, 0) for breed in df_closeness['Breed']]

        filename_without_extension = os.path.splitext(os.path.basename(input_fasta_file))[0]

        table_output_file = os.path.join(dog_output_directory,
                                        f"{filename_without_extension}_closeness_table.tsv")
        df_closeness.to_csv(table_output_file, sep='\t', index=False)
        print(f"Table of Distance to Unknown Breed with p-values saved to: {table_output_file}")

        visualize_phylogenetic_tree(output_tree_file)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_master_script()
