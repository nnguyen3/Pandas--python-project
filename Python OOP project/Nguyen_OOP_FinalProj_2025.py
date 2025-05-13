## RENAME this file YourLastName_OOP_FinalProject_2023.py

##Assignment: Add to the constructor and methods of a parent class and child classes
##            which inherit the base class properties. NOTE: You are not allowed
##            to import any specialized libraries for this project (e.g., no Biopython)
##            The idea is for you to write these methods from scratch.

## Begin with the parent Seq class and the child DNA class we created in lecture below.
## 



#  Constructor:
#  (1) Use the string functions upper and strip to clean up self.sequence.
#  (2) Add a variable self.kmers to the constructor and make it equal to an empty list.

#  Methods:
#  (1) Add a method called make_kmers that makes overlapping kmers of a given length from self.sequence
#      appends these to self.kmers. Default kmer parameter=3.
#  (2) Add a method called fasta that returns a fasta formatted string like this:
#      >species gene
#      AGATTGATAGATAGATAT
class Seq:
    def __init__(self,sequence, gene, species):
        self.sequence= sequence.upper().strip()
        self.gene = gene 
        self.species= species
        self.kmers= [] #empty list for kmer
    
    def __str__(self):
        return str(self.species) + " " + str(self.gene) + " : " + str(self.sequence)

    def print_record(self):
       print(self) #this will print from  _str_
    
    #1) Add a method called make_kmers that makes overlapping kmers of a given length from self.sequence
#      appends these to self.kmers. Default kmer parameter=3.
    def make_kmers(self, k= 3): 
        self.kmers= [] #empty list for kmer
        for i in range(len(self.sequence) - k +1 ):
            #this will run loop one by one through every position in the sequence
            # -k means that we need at least k letters, for ex AGCTV then after kmer there will be TV and V left
            # without -k +1 then this sequence enc up to have incomplete kmer , 
        # grab from the sequence that is 'k' letters long , so if k=3 then grab 3 like TV and V
            kmer= self.sequence[i: i +k]
            # this to grab string length k, starting at position i
        # Add this to the kmers list
            self.kmers.append(kmer)
        return self.kmers
        
    def fasta(self):
        return ">" + str(self.species) + " " + str(self.gene) + "\n" + str(self.sequence)


### DNA Class: INHERITS Seq class
#   
#  Constructor:
#  Use re.sub to change any non nucleotide characters in self.sequence into an 'N'.
#      re.sub('[^ATGCU]','N',sequence) will change any character that is not a
#      capital A, T, G, C or U into an N. (Seq already uppercases and strips.)

#  Methods:
#  (1) Add a method called print_info that is like print_record, but adds geneid and an
#      empty space to the beginning of the string.
#  (2) Add a method called reverse_complement that returns the reverse complement of
#      self.sequence
#  (3) Add a method called six_frames that returns all 6 frames of self.sequence
#      This include the 3 forward frames, and the 3 reverse complement frames

import re
class DNA (Seq):
    def __init__(self, sequence, gene, species,gene_id):
        # **kwargs: give a keyword , allow to add on in instance
        super().__init__(sequence, gene, species)
        self.gene_id= gene_id
        self.sequence=re.sub('[^ATGCU]','N',self.sequence) 

    def analysis (self):
        G= 0
        C= 0
        for b in self.sequence:
            if b == "G":
                G += 1
            elif b == "C":
                C += 1
        return G ,C

    def print_info (self):  #adds geneid and an
    # empty space to the beginning of the string
        return str(self.gene_id) + " " + str(self.species) + " " + str(self.gene) + " : " + str(self.sequence)


    

    def reverse_complement(self):
        #define which base complement using dictionary
        complement={'A':'T',
                    'T':'A',
                    'G':'C',
                    'C':'G'}
        reversed_comp= '' # empty string for reversed complement
        # loop through the sequence  backward
        for i in range (len(self.sequence)-1,-1,-1):
            # -1,-1,-1 means start, stop, and step
            # if the length =5 for ex, then it would start at position 4, stop at 0 but we want to include position 0 
            # so -1 for stop , then step -1 is going backward 
            base = self.sequence[i] #grab the base from the end, because for loop tell i to start at the end and going backward
            rev_base=complement.get(base, 'N') # look up in the dictionary, if not ATCG then use N
            reversed_comp += rev_base # add the complement to  reversed comp string
        return reversed_comp
    
    def six_frames(self):
    # each frame start reading the sequence from different position, in groups of 3 (codons)
    # my plan 
    # 1. create list to store 6 frames
    # 2. add 3 frame for forward, 3 frame for backward
    # reversed_comp for reverse strand
    # 3. add 3 reversed from reversed complement
    # then ruturn 
        frames= [] # start with empty
    #forward frame starting at position 0 , 1 ,and 2
        frames.append(self.sequence[0:])  # frame 1
        frames.append(self.sequence[1:])    #frame 2
        frames.append(self.sequence[2:])    #frame 3

        reversed_comp= self.reverse_complement() # grab the reverse complement
    
    # reverse frame starting at 0, 1, 2 in reverse order
        frames.append(reversed_comp[0:])
        frames.append(reversed_comp[1:])
        frames.append(reversed_comp[2:])

        return frames

### RNA Class:  INHERITS DNA class
#  
#  Construtor:
#  Use the super() function (see DNA Class example).
#  (1) Automatically change all Ts to Us in self.sequence. 
#  (2) Add self.codons equals to an empty list

#  Methods:
#  (1) Add make_codons which breaks the self.sequence into 3 letter codons
#      and appends these codons to self.codons unless they are less than 3 letters long.
#  (2) Add translate which uses the Global Variable standard_code below to
#      translate the codons in self.codons and returns a protein sequence.

standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

class RNA(DNA):
    def __init__(self, sequence, gene, species, gene_id):
        rna_seq= sequence.upper().replace("T","U")
        #convert T to U
        super().__init__(rna_seq, gene, species, gene_id)
        # why didnt i use just sequence like DNA
        # i create rna_seq so this class will use seq with U instead of T like DNA, if I kept sequence then I will passing DNA sequence to RNA
        self.codons= [] #make an empty list to store codon
        
    def make_codons(self):
        # loop throug sequence
        # grab 3 letter
        self.codons=[] #start empty list of codon
        for i in range(0, len(self.sequence), 3):
            codon = self.sequence[i:i+3] # grab 3 codon from sequence
            if len(codon) == 3: # to ensure to keep full 3 codons
                self.codons.append(codon) # full 3 codon then add to codon list
        return self.codons
    
    
    def translate(self):
        #translate codon to protein
        protein="" #start with empty string
        # loop through every codon in self.codon
        for codon in self.codons:
            protein += standard_code.get(codon, "X") # look up dict, if can't match with codon then use X
            # standard_code[codon]  # look for codon in dictionary then add to protein
            # += is to add amino that has been translate by standard_code to protein string
        return protein

    
    
 ### Protein Class: INHERITS Seq class
#
#  Construtor:
#  Use the super() function (see DNA Class example).
#  Use re.sub to change any non LETTER characters in self.sequence into an 'X'.

#  Methods:
#  The next 2 methods use a kyte_doolittle and the aa_mol_weights dictionaries.
#  (2) Add total_hydro, which return the sum of the total hydrophobicity of a self.sequence
#  (3) Add mol_weight, which returns the total molecular weight of the protein
#      sequence assigned to the protein object.    

kyte_doolittle={'A':1.8,'C':2.5,'D':-3.5,'E':-3.5,'F':2.8,'G':-0.4,'H':-3.2,'I':4.5,'K':-3.9,'L':3.8,
                'M':1.9,'N':-3.5,'P':-1.6,'Q':-3.5,'R':-4.5,'S':-0.8,'T':-0.7,'V':4.2,'W':-0.9,'X':0,'Y':-1.3}

aa_mol_weights={'A':89.09,'C':121.15,'D':133.1,'E':147.13,'F':165.19,
                'G':75.07,'H':155.16,'I':131.17,'K':146.19,'L':131.17,
                'M':149.21,'N':132.12,'P':115.13,'Q':146.15,'R':174.2,
                'S':105.09,'T':119.12,'V':117.15,'W':204.23,'X':0,'Y':181.19}

class Protein(Seq):
    def __init__(self, sequence, gene, species,gene_id=None): 
        # first i only put 3 argument for protein but got error when i tested it, so i put gen_id as optional
        pro_seq= re.sub('[^A-Z]','X',sequence.upper()) # [^A-Z]= not letter from A-Z then make it X
        super().__init__(pro_seq, gene, species) #only 3 arguments
        self.gene_id = gene_id #store extra info
    
    def total_hydro(self):
        # Calculate total hydrophobicity using the kyte_doolittle table
        total = 0 # start with 0 total hydrophobicity
        #total hydrophobicity (aa) of a self.sequence
        # loop through sequence to check for aa
        for aa in self.sequence:
            hydro = kyte_doolittle.get(aa,0) 
            #from dictionary kyte_doolittle
            #get(aa,0) so if not found aa from dict then use 0 instead to not causing any error
            total += hydro #adding each hydro to total
        return total


#similar concept with total hydro
    def mol_weight(self):
        total1 = 0  # Start at 0
        for aa in self.sequence:
            weight = aa_mol_weights.get(aa, 0)  # Look up weight in dict aa_mol_weight,=0 if not found
            total1 += weight  # add value that found matching in dict to total
        return total1



















    

x=DNA("G","tmp","m",000)





