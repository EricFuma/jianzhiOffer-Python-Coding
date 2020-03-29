'''
1. 给定3*n 数组nums， 每列选择一个数， 最终形成一个列表L(1 * n)， 求最小的 sum( abs( L[ i ] - L[ i -1]  ))
'''
# 输入样例
arr = [
    [2, 5, 7, 3, 8, 6],
    [3, 1, 5, 4, 2, 4],
    [7, 9 ,8, 2, 5, 7]
    ]


length = len(arr[0])
res = [[0] for i in range(len(arr))]

for i in range(1, length):
    for j in range(len(arr)):
        num = min(arr[k][i-1]+abs(arr[j][i]-arr[k][i-1]) for k in range(len(arr)))
        res[j].append(num)
print(min(res[j][-1] for j in range(len(arr))))

'''
维特比算法基于一个条件：当前状态只与前一个状态有关，不受其他状态影响（HMM假设）
那我们的题目是否满足这个条件呢？首先我们在res每一列k上存储的是到当前位置i的“长度为k+1的最短路径”.当前要抉择的位置为pos，
- 当 pos==0 的时候，显然是满足的
- 当 pos!=0 的时候，由于我们在pos-1存放的是0~pos的最短路径，所以对于当前位置我们遍历前一列去最小就可以了


我觉得更重要的是要把这个问题抽象成一个“寻找最优路径”的问题
它又满足HMM假设，自然会想到用维特比算法来做
'''

