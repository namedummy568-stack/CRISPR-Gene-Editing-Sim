def edit_gene(dna_sequence, target_sequence, replacement_sequence):
    """
    Simulates gene editing by replacing a target sequence in a DNA sequence.

    Args:
        dna_sequence (str): The original DNA sequence.
        target_sequence (str): The sequence to be replaced.
        replacement_sequence (str): The sequence to replace the target with.

    Returns:
        str: The modified DNA sequence.
    """
    return dna_sequence.replace(target_sequence, replacement_sequence)
