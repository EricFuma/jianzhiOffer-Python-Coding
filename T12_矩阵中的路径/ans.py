class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 我的第二种方法：用 dict 来存储已经走过的节点，这样每次确定节点是否走过的时候，都只需要 O(1) 了

        if not word:
            return True
        if not board:
            return False

        def DFS(i, j, seen):
            if len(seen) == len(word):
                return True
            for op in ops:
                x, y = i+op[0], j+op[1]
                if 0<=x<m and 0<=y<n and board[x][y] == word[len(seen)] and (x,y) not in seen:
                    seen[(x,y)] = 1
                    if DFS(x, y, seen):
                        return True
                    else:
                        seen.pop((x,y))
            return False


        ops = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if DFS(i, j, {(i, j):1}):
                        return True
        return False



    
        # 我的一开始方法：用的是一个 列标 来存储 visited，但这样每次确定点的有无都需要 O(N)，不高效
        '''
        def dfs(i, j, visited, k):
            if k == len(word):
                return True

            ops = [[0,1], [0,-1], [-1,0], [1,0]]
            for op in ops:
                x, y = i+op[0], j+op[1]
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == word[k] and [x,y] not in visited and dfs(x, y, visited+[[x, y]], k+1):
                    return True            
            return False
        
        if not word:
            return True
        if not board:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, [[i, j]], 1):
                        return True
        return False
        '''
