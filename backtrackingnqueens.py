class Solution:
    def solveNQueens(self, n):
        res = set()		# Storing the coordinates of the queen placed on each line
        # 
        def find_pos(row_index, queen, n):
            for j in range(n):
                if pos_available(queen, (row_index, j)):
                    queen[row_index] = j
                    if row_index == n-1:    # Already the last line and found the location where you can put it
                        res.add(tuple(queen))
                        return
                    else:   # 
                        find_pos(row_index+1, queen, n)
		# Verify that the current location is available
        def pos_available(queen, pos):
            #   According to 0~i-1 line
            for i in range(pos[0]):
                if queen[i] == pos[1]:  # 
                    return False
                elif abs(i-pos[0]) == abs(queen[i]-pos[1]): #   diagonal
                    return False
            return True
		# Print the coordinate form as Q...form
        def plot_queen(queen, n):
            out = []
            for i in range(n):
                s = '.' * queen[i] + 'Q' * 1 + '.' * (n-queen[i]-1)
                out.append(s)
            return out

        # -1 Actually has no effect
        queen = [-1 for _ in range(n)]  # initial position
        # Recursion Starting from line 0
        find_pos(0, queen, n)
        out = []
        for t in res:
            out.append(plot_queen(t, n))
        return out
