from itertools import permutations  
print("Computing all permutation of the following list")  
print(list(permutations([3,"Python"],2)))  
print("Permutations of following string")  
print(list(permutations('AB')))  
print("Permutation of the given container is:")  
print(list(permutations(range(3),2)))  
print(list(permutations(range(3),3)))  