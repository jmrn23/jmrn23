L=input()
a=[int(b) for b in L.split()]

even= list(filter(lambda x: (x%2)==0,a))
odd= list(filter(lambda x: (x%2)!=0,a))
print("Even")
print(even)
print("Odd")
print(odd)

