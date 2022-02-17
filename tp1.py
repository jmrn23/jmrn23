
#Julie Moreno 32
#yo
#test
#test2
#test3
#test4
#test5
#test 6 
#test 6
#test 7
#test 8
#test 9
#test 10

#syracuse
"""
f=open("syracuse.txt","r+")
n=int(f.readline())
#n=int(input())

if n>0 :
    while n!=1 :
         if n%2==0:
             n=n/2
         else :
              n=(3*n)+1

f.write(str(int(n)))              
print(int(n))       
f.close()
"""
#fin syracuse normal




#syracuse POO

class syracuse :

    def algo(self,n) :

        if n>0 :
             while n!=1 :
                 if n%2==0:
                      n=n/2
                 else :
                     n=(3*n)+1
             return int(n)

f=open("syracuse.txt","r+")
i=int(f.readline())
s=syracuse()
f.write(str(s.algo(i)))
f.close()

#fin syracuse POO



#egyptienne
"""
a=int(input())
b=int(input())
sum=0

while b!=0:
    if b%2 !=0 :
        sum+=a
        a*=2
        b//=2
    else :
        a*=2
        b//=2

print(sum)
"""
#fin egyptienne
