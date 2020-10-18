#gcd.py

def gcd(n, m):


    while m:
        n, m = m, n%m
    return n

# JA: You should have a program to call this
