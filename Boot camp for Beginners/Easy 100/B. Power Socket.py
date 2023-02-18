import sys
input = sys.stdin.readline

a, b = map(int, input().split())
con = 1
ans = 0
 
while con < b:
    con += a - 1
    ans += 1
 
print(ans)