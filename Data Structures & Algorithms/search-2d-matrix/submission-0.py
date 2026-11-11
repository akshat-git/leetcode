class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = 0
        b = len(matrix)-1
        while a<=b:
            m = (a+b)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                b = m-1
            elif matrix[m][0] < target:
                a = m+1
        row = matrix[b]

        a = 0
        b = len(row)-1
        while a<=b:
            m = (a+b)//2
            if row[m] == target:
                return True
            elif row[m] > target:
                b = m-1
            elif row[m] < target:
                a = m+1
        return False