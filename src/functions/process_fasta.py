"""
Contains functions for processing FASTA files.
"""

def process_fasta(input_fasta, align=True, output_dir=None):
    """
    Process a FASTA file, extracting sequence records and relevant information.
    
    Args:
        input_fasta (str): Path to the input FASTA file.
        align (bool): Whether to perform alignment (default is True).
        output_dir (str): Output directory for saving results (default is None).
    
    Returns:
        Tuple: A tuple containing alignment, output FASTA file, output directory, breed names, and accession numbers.
    """

     seq_records = []

    with open(input_fasta, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            seq_records.append(record)

    breed_names = []
    accession_numbers = []
    for record in seq_records:
        match = re.search(r'\bbreed=([^\]]+)', record.description)
        if match:
            breed_name = match.group(1).replace(' ', '_')
            if "Mixed" in breed_name:
                country_match = re.search(r'\[country=([^\]]+)\]', record.description)
                if country_match:
                    country = country_match.group(1)
                    breed_name += f"_{country}"
            breed_names.append(breed_name)
        else:
            breed_names.append("unknown")

        accession_match = re.search(r'\|([^|]+)\|', record.description)
        if accession_match:
            accession_numbers.append(accession_match.group(1))
        else:
            accession_numbers.append(None)

    if align:
        alignment = MultipleSeqAlignment(seq_records)
        if output_dir is None:
            results_dir = os.path.join(os.path.dirname(input_fasta), 'results')
            os.makedirs(results_dir, exist_ok=True)
        else:
            results_dir = output_dir

        filename_without_extension = os.path.splitext(os.path.basename(input_fasta))[0]
        output_filename = f"{filename_without_extension}_aligned.fa"

        output_fasta = os.path.join(results_dir, output_filename)

        with open(output_fasta, 'w') as output_file:
            AlignIO.write(alignment, output_file, 'fasta')
        
        print(f"Alignment saved to: {output_fasta}")
    else:
        alignment = None
        output_fasta = None
        results_dir = None

    return alignment, output_fasta, results_dir, breed_names, accession_numbers
        
        