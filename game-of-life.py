from copy import deepcopy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        cp_board = deepcopy(board)

        x_size = len(board[0])
        y_size = len(board)
        if not x_size:
            return board
        bfs=[(0, 0)]
        points = [(1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1)]
        visted = set()
        while bfs:
            x, y = bfs.pop()
            visted.add((x , y))   
            count = 0
            for i, j in points:
                if 0<=i + x < x_size and 0<= j + y <y_size:
                    if cp_board[y+j][x+i] == 1:
                        count += 1
                    if (i + x , j + y) not in visted and (i + x , j + y) not in bfs:
                        bfs.append((i + x , j + y))
            # print count , (y, x)
            if count < 2:
                board[y][x] = 0
            if count == 2:
                board[y][x] = cp_board[y][x]
            if count > 3:
                board[y][x] = 0
            if count == 3:
                board[y][x] = 1
        
        return board

# 记录下之前的状态，如果需要原地的话那么使用 其他数字表示状态例如 2， 3 4 此类数字表示 由1->0 由0->1 这样可以保证结果不受影响