import math 

def solve():
    n = int(input())
    if n == 1:
        print(0)
    else:
        sqrt_n = int(math.sqrt(n))
        ans = 0
        for i in range(2, sqrt_n + 1):
            if n%i == 0:
                if i == n//i:
                    ans += i 
                else:
                    ans += i + n//i 
        ans += 1
        print(ans)

T = int(input())
for _ in range(T):
    solve()
