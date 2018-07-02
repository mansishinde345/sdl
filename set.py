A=set([1,2,3,4])
B=set([ 3,4,5,6])

print('Set A is:')
print(A)
print(len(A))
print(6 in A)



print(1 in A)
print('Set B is:')
print(B)
print(len(B))
      
print('Union')
print(A|B)

print('Intersection')
print(A&B)

print('Difference')
print(A-B)

print('Symmetric difference')
print(A^B)

print("All set operations using predefined function")
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
