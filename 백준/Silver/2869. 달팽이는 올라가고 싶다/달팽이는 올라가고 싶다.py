A,B,V = map(int, input().split())

X, Y = V-A, A-B

print(X//Y+1 if X//Y==X/Y else X//Y+2)