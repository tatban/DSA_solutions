# Spiral Matrix (reading)(LeetCode 54)
# Given an m x n matrix, return all elements of the matrix in spiral order. (Clockwise order i.e. starting from going right in first row)

#############################SOLUTION#######################################
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n-1
        up, dn = 0, m-1
        res = []

        while up<=dn and left<=right:
            for i in range(left,right+1):
                res.append(matrix[up][i])
            up+=1
            for i in range(up,dn+1):
                res.append(matrix[i][right])
            right-=1
            if up <= dn:  # for non square matrix
                for i in range(right,left-1,-1):
                    res.append(matrix[dn][i])
                dn-=1
            if left <= right:  # for non square matrix
                for i in range(dn,up-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res

##########################ALTERNATIVE SOLUUTIONS###################
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        r_idx, c_idx = 0,0
        dr, dc = 0, 1
        res = []

        for _ in range(m*n):
            res.append(matrix[r_idx][c_idx])
            matrix[r_idx][c_idx] = "#"

            if not 0 <= r_idx + dr <m or not 0 <= c_idx + dc <n or matrix[r_idx + dr][c_idx + dc] == "#":
                dr, dc = dc, -dr

            r_idx += dr
            c_idx += dc

        return res
