# Python OOP and Pandas Projects

This repository include Python projects and python practice for BIOL 668. Applying object-oriented programming (OOP) concepts and data analysis using Pandas,...

---

# Folder Descriptions
# Required file:
- KRAS.fasta
- Kras_genbank.gb
- OOPTestProject2025.pdf
- SeqRecord.py
- 04A_Biopython_Tutorial_LSH-1.ipny
- opuntia.dnd
  
# `Python OOP Project part 2`
- Contains the second part of the final OOP project.
- Use to see how classes can model biological systems.
- Include Biopython tutorial ( seqrecord, get familiar with biopython, read fasta and genbank file, manipulate seq objects, create phylogeny tree)
- investigating properties of the SeqRecord class

# `Python OOP lab 1`
- OOP practice.
- Focuses on defining classes, using methods, and understanding inheritance.

# `Python OOP project`
- build 3 class OOP concept using biological seq
- clean up seq
- reverse_complement to return reverse complement of seq
- generate 6 reading frames ( 3 forward, 3 reverse)
- translate codons
# Instruction for Python OOP project
Download the required file , then create class Seq, DNA, RNA, and protein that inherit from parent class (Seq).
To inherit , for ex:
class DNA(Seq):
    def __init__(self, sequence, gene, species, gene_id, **kwargs):
        super().__init__(sequence, gene, species)
Run doctest to make sure the function code is correct and run smoothly:
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


# `pandas and python`
- PandasScipy Practice
- Includes visualizations, statistical analysis, and exploratory data analysis with NumPy and SciPy.

---
# How to use 
- to run python script, open terminal , cd to the folder that have the file and run :
in bash, run:
python filename.py or python NGUYEN_OOP_FinalProject_2023.py
