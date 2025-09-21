# CRISPR-Gene-Editing-Sim

This repository contains a simulated gene-editing algorithm implemented in Python.

## `edit_gene` Function

The `edit_gene` function simulates the process of gene editing by replacing a specified target DNA sequence with a replacement sequence within a given DNA strand. This simplified model helps in understanding the basic concept of sequence-specific gene modification.

### Usage

```python
from gene_editor import edit_gene

dna = "ATGCGTACGTACGTACGTAGCTAGCTACGTAGCT"
target = "GTACGT"
replacement = "GGCCAA"

modified_dna = edit_gene(dna, target, replacement)
print(f"Original DNA: {dna}")
print(f"Modified DNA: {modified_dna}")
```
