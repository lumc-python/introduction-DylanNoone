#Excercise two 
DNA = ('ACGTACGTACGTTTATTTTATTTTATTTTATTTTATT')
range(len(DNA))

for start in range(len(DNA)-2):
    print(DNA[start : start+3])
    
triplets = set()
for start in range(len(DNA)-2):
    triplets.add(DNA[start : start+3])
print(triplets)