#Modify your function to use a dictionary with substring counts.
# Use the substrings as dictionary keys.
# Use the counts as dictionary values.
# Have the function return the dictionary.
# Add a docstring to the function.
# Use the function to print k-mer counts for some strings.

DNA = input('what is dna')

k = range(len(DNA))

def strings (k, DNA):
    
    triplets = set()
    for start in range(len(DNA)-2):
        a_triplet = DNA[start:start+3]
        triplets.add(a_triplet)

kmer = (len(DNA.split(a_triplet))-1)

dictionary = {a_triplet : kmer}
print(dictionary) 
