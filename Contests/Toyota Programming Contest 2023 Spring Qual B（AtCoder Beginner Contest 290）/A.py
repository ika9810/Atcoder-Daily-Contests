import sys
input = sys.stdin.readline

N, M = map(int,input().split())
res = 0
score = list(map(int,input().split("\n")[0].split(" ")))
solved = list(map(int,input().split("\n")[0].split(" ")))
for num in solved:
    res += score[num-1]
print(res)