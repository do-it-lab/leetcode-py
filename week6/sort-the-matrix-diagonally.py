"""

Given a m * n matrix mat of integers,

sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.


Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

https://leetcode.com/problems/sort-the-matrix-diagonally/

"""

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
