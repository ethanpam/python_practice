def complementaryDna(strand: str) -> str:
    """
    Return the complementary DNA strand.

    Parameters:
        strand (str): DNA sequence containing characters 'A', 'T', 'C', 'G'.

    Returns:
        str: The complementary DNA strand.
    """
    complementary = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(complementary[i] for i in strand)

def main():
    strand = str(input("What is thes strand?: "))
    print(complementaryDna(strand))

if __name__ == "__main__":
    main()