# Spiral Matrix II (LeetCode 59)
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order. (clockwise spiral: starting from going right from the first row)

###################solution###################
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nrows = ncols = n
        top = 0
        bot = nrows -1
        left = 0
        right = ncols - 1
        curr_value = 1
        res = [[0]*ncols for r in range(nrows)]  # [[0]*ncols]*nrows doesn't work, as rows don't get duplicated and refer to one single row !!!
        dir = 0  # tracking of direction
        while top <= bot and left <= right:
            dir_ = dir % 4
            if dir_ == 0: # east
                for j in range(left,right+1):
                    res[top][j] = curr_value
                    curr_value+=1
                top += 1
            elif dir_ == 1: # south
                for i in range(top,bot+1):
                    res[i][right] = curr_value
                    curr_value+=1
                right -= 1
            elif dir_ == 2: # west
                for j in range(right, left-1,-1):
                    res[bot][j] = curr_value
                    curr_value+=1
                bot -= 1
            elif dir_ == 3: # north
                for i in range(bot, top-1, -1):
                    res[i][left] = curr_value
                    curr_value+=1
                left += 1
            dir += 1
        return res
