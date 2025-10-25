#Complementary DNA              10-25-25
#Given a string representing a DNA sequence, return its complementary strand using the following rules:

#DNA consists of the letters "A", "C", "G", and "T".
#The letters "A" and "T" complement each other.
#The letters "C" and "G" complement each other.
#For example, given "ACGT", return "TGCA".


'''
Converts a strand of string into its complementary strand

@param strand - DNA strand consisting of either 'A T C G'
@return - Complementary Dna
'''
def complementary_dna(strand):
    complementary = ""
    for i in strand:
        if i == "A":
            complementary = complementary + "T"
        elif i == "T":
            complementary = complementary + "A"
        elif i == "C":
            complementary = complementary + "G"
        elif i == "G":
            complementary = complementary + "C"
    return complementary

def main():
    strand = str(input("Strand here: "))
    print(complementary_dna(strand))

if __name__ == "__main__":
    main()