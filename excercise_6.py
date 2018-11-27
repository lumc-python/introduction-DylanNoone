## (1/2)
#Remember the previous exercise of finding (unique) substrings of length 3.
#- Make a function from your implementation.
#- Have *k* as an argument to the function.
#- Test the function on several input strings.
DNA = input('what is dna')

k = range(len(DNA))

def strings (k, DNA):
    
    triplets = set()
    
    for start in range(len(DNA)-2):
        a_triplet = DNA[start:start+3]
        print(a_triplet)    
        triplets.add(a_triplet)
    return triplets
print(strings(k, DNA))
    