class Solution:
    def spiralOrder(self, matrix):
        result = []

        while matrix:
            # 1. First row → left to right
            result += matrix.pop(0)

            # 2. Last column → top to bottom
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            # 3. Last row → right to left
            if matrix:
                result += matrix.pop()[::-1]

            # 4. First column → bottom to top
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result