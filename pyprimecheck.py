import math

def isPrime(n) :
    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False
 
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
 
    return True

def primeFactors(n):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        print (2),
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            print (i),
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print (n)


if(isPrime(<Prime Goes Here>)) :
    print(" true")
else :
   print(" false")


#Prime Factorization Section
n = <Prime Goes Here>
primeFactors(n)




