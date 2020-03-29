
import sys
'''
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
a = list(map(int, line.split()))
line = sys.stdin.readline().strip()
b = list(map(int, line.split()))
'''


n, m = 5, 5
a = [10, 20, 30, 40, 50]
b = [4, 5, 6, 7, 8]
'''
n, m = 3, 3
a = [10, 20, 30]
b = [4, 5, 6]
'''

# 两个list同时排序
# https://blog.csdn.net/rosefun96/article/details/104768294/

b, a = zip(*sorted(zip(b, a), reverse=True))
b, a = [0]+list(b), [0]+list(a)
f = [[0]*(m+1) for i in range(n+1)]
# f[i][j] 从a数组前i个数中选j个数的最大和
for i in range(1, n+1):
    for j in range(1, min(i+1, m+1)):
        f[i][j] = max(f[i-1][j], f[i-1][j-1]+a[i]-b[i]*(j-1))

print(f[n][m])

# 设 f[i][j] 为 “从a数组前i个数中依次取出j个数的和的最大值”
# 则有状态转移方程： f[i][j] = max(f[i-1][j], f[i-1][j-1]+a[i]-b[i]*(j-1))
