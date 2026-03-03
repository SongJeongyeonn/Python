import sys
input = sys.stdin.readline
n,m = map(int, input(),split())
A = list(map(int, input().split()))
S = [0]*n
C = [0]*m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]