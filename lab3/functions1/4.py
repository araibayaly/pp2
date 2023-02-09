def prime(n):
  if n < 2:
    return False
  for i in range(2, n):
    if  n%i == 0:
        return False
  return True

def filter_prime(N):
    primes=[]
    for n in N:
        if prime(n):
            primes.append(n)
    return primes 

N = [1 ,6 ,7 ,46 ,13 ,35 , 57, 78]
print(filter_prime(N))