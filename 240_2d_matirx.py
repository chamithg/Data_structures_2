class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if r[0] == target or r[-1] == target : return True
            if r[0]< target < r[-1]:
                for c in r:
                    if c == target: return True

        return False