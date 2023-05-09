#Part 1

n = int(input("Fibonacci Sequence Up To... "))

def fibonnaci(n):
    if n < 0:
        print("Value cannot be less than 0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
print (fibonnaci(n))

#Part 2

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

def gcd(a,b):
    if a < b:
        (a,b) = (b,a)
    if (a%b) == 0:
        return b
    else:
        return (gcd(b, a%b))
print (gcd(a,b))

#Part 3

s1 = str(input("Enter string one for comparison: "))
s2 = str(input("Enter string two for comparison: "))

def compareTo(s1, s2):
    if s1 < s2:
        return (0-1)
    elif s1 == s2:
        return (0)
    elif s1 > s2:
        return (0+1)
    else:
        return ("Not a string")