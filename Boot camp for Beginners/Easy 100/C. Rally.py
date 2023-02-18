import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int,input().split("\n")[0].split(" ")))

arr = []
for j in range(0,101):
    res = 0
    for i in range(len(x)):
        res += (x[i]-j)**2
    arr.append(res)
print(min(arr))
