import sys
input = sys.stdin.readline

N, K = map(int,input().split())
S = list(input().split("\n")[0])
res = ""
for i in range(len(S)):
    if S[i] == "o":
        if K > 0:
            res+="o"
            K = K - 1
        else:
            res+="x"*(N-len(res))
            break
    else:
        res+="x"
print(res)