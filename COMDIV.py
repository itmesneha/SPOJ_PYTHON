# still gives TLE but this is correct algorithm

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def num_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if i * i == n:
            count += 1
            continue
        if n % i == 0:
            count += 2
    return count

t = int(input())
for case in range(t):
    A = list(map(int, input().split()))
    print(num_divisors(gcd(A[0], A[1])))
