import sys
import math
input = sys.stdin.readline

N = int(input())
chk = True
for i in range(N):
    if math.floor((N-i)* 1.08) == N:
        print(N-i)
        chk = False
if chk:
    print(":(")