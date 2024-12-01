import numpy
import random

class DNA(object):
    """DNA manipulation \n
    Attibutes DNA_chain: sequence, frequencies, length"""
    def __init__(self, sequence): # NEVER ACCESS THIS DATA ATRIBUTES OUTSIDE THE CLASS
        self.sequence = sequence
        self.freqs = self.measure_freqs()
        #?self.directory=directory  
        self.length = len(self.sequence)

    def __str__(self):
        self.length=len(self.sequence)
        self.freqs = self.measure_freqs()
        return str(self.length)+ ","+ str(self.sequence)+ ","+ str(self.freqs)#+ str(self.directory)
    
    def create_seq(self, length):
        """Create a random sequence: \n 
        length = provide desired length"""
        nuclFreq=[0.2,0.3,0.3,0.2]      #Make nucleotides' frequency to be slightly more realistic
        nucleotidos=["A","C","G","T"]
        self.sequence=numpy.random.choice(nucleotidos, size=length, p=nuclFreq)
        self.sequence=numpy.array(self.sequence) #Avoiding future array problems:changing array to numpy array
        self.sequence = ''.join(self.sequence.tolist()) #numpy array to list and join into STRING
        return self.sequence
    #Metodo:Revisar si la secuencia contiene solo bases correctas.
    def validate(self):
        for base in self.sequence:
            if base not in "ATCG":
                return False
        return True     
    #Metodo:Contar cantidad de cada tipo de nucleótido
    def measure_freqs(self):
        self.freqs={"A":0, "T":0, "G":0, "C":0}
        for nucleotido in self.sequence:  
            if nucleotido == "A":
                self.freqs["A"]+=1
            elif nucleotido == "T":
                self.freqs["T"]+=1
            elif nucleotido == "G":
                self.freqs["G"]+=1
            elif nucleotido == "C":
                self.freqs["C"]+=1
        return self.freqs
    #Metodo: Count subsequences 
    def count_subseq(self,chain_in):
        """Count the number of times that appears a given subsequence
        Parameters: 
            chain-in -> the dinucleotide or sequence to find"""
        chain_in_count=0
        chains_positions=[]
        chain_in_length=len(chain_in)
        i=0
        while i<=len(self.sequence)-chain_in_length:
            find=self.sequence[i:i+chain_in_length]
            if chain_in==find:
                chains_positions.append(i)
                chain_in_count+=1
                i+=chain_in_length 
                #to move index forward by the length of the subsequence to avoid overlap
            else:
                i+=1    #otherwise, move to next character
        return chain_in_count, chains_positions 
    #Metodo: Obtaining reverse and complementary chain
    def synt_complement (self):
        sequence=self.sequence
        reverse=sequence[::-1]
        to_replace={"A":"T","T":"A","G":"C","C":"G"}
        result=[]
        for nucl in self.sequence:
            result+=to_replace[nucl]
        complementary=''.join(result)
        return sequence,reverse,complementary
    #Method: Measure CG_percentages
    def cg_percentage (self):
        CG_count=0
        total=0
        #Calculate total number of CG dinucleotides
        for i in range (len(self.sequence)-1):
            dinucleotide=self.sequence[i:i+2]
            if dinucleotide == "CG":
                CG_count +=1
            total +=1
        if total == 0:
            return 0
        return (CG_count*100)/total  #f"CG%={cg_percentage:.2f}">>FOR PRINTING purposes:to get 2 floating points
    #Method to mutate sequences:
    def mutate(self,num_mutations):
        positions=random.sample(range(0,len(self.sequence)),num_mutations) #for given number of unique positions
        result=list(self.sequence)
        for i in range(len(self.sequence)):
            if i in positions:
                if result [i]=="A":
                    result[i]=random.choice(["C","G","T"])
                elif result [i]=="C":
                    result[i]=random.choice(["A","G","T"])
                elif result [i]=="G":
                    result[i]=random.choice(["C","A","T"])
                elif result [i]=="T":
                    result[i]=random.choice(["C","G","A"])
        return ''.join(result) # Intentar devolver los dos argumentos: mutated_seq, num_mutations
    #Method to re-generate DNA??? QUIZAS NO HACER
    def set_seq (self, newseq=""):
        self.sequence = newseq
# ------------------------------------------------------
#sequence1 = DNA.create_seq(DNA, 20)
#print("Sequence 1 is: ", sequence1)
#print(type(sequence1))
#
#sec=DNA("AAGTTCGTCAGTCACCTGGACGGTC")
#print("Sequence 2 is: ", sec)
#print(type(sec))
#
#largo=int(input("Enter a sequence length: "))
#sequence2=DNA("")
#seq=sequence2.create_seq(largo)
#print("Sequence 3 is :", seq)
#print("Another form of Sequence 3 is :", DNA(seq))
#print("Sequence 4th type is: ", type(sequence2))
# ------------------------------------------------------
#print(sequence.measure_freqs())
#print(sequence.validate())
#subseq="CG"
#print(sequence.count_subseq(subseq))
#print(sequence.cg_percentage())
#print(sequence.mutate(5))
#print(DNA.__dict__.keys())
#print(DNA.__dict__.values())
#print(sequence.__dict__.keys())
#print(sequence.__dict__.values())
# ------------------------------------------------------
