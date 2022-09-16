# intraverse function for integers
def intreverse(n):
  reversed_n = 0
  while n > 0:
    (d, n) = (n%10, n//10)
    reversed_n = 10*reversed_n + d
  return(reversed_n)

## matching string function
def matched(s):
  nested = 0
  for i in range(0, len(s)):
    if s[i] == "(":
      nested = nested + 1
    elif s[i] == ")":
      nested = nested - 1
      if nested < 0:
        return(False)
  return(nested == 0)


## factoring integer

def factor(n):
  factorlist = []
  for i in range(1,n+1):
    if n%i == 0:
      factorlist.append(i)
  return(factorlist)

## to check prime number

def isprime(n):
  return(factor(n) == [1, n])

# sum of primes

def sumprimes(l):
  sum = 0
  for i in range(0,len(l)):
    if isprime(l[i]):
      sum = sum + int(l[i])
  return(sum)