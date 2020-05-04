"""

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

https://leetcode.com/problems/set-matrix-zeroes/

"""


class Solution(object):
    """

    matrix 의 모든 공간이 zero 일 경우(WorstCase),
    matrix 를 그대로 순회 한다면, O(mn) space 사용하게 됨
    순회 할 때, row, col 중복을 제거한다면, WorstCase 에서 O(m+n) space 사용하게 됨
    근데 그거 말고 constant space 를 쓸 수 있게 하라고?

    O(m+n) space
    O(n^2) time

    """

    def setZeroes(self, matrix):

        row_nums, col_nums = self.findZeroes(matrix)
        self.pushBomb(matrix, col_nums=col_nums, row_nums=row_nums)


    def findZeroesByStraightForward(self, matrix):

        rows = []
        cols = []

        for row_idx, row in enumerate(matrix):
            for col_idx, item in enumerate(row):
                if item == 0:
                    rows.append(row_idx)
                    cols.append(col_idx)

        return rows, cols

    def findZeroes(self, matrix):

        rows = set()
        cols = set()

        for row_idx, row in enumerate(matrix):
            for col_idx, item in enumerate(row):
                if item == 0:
                    rows.add(row_idx)
                    cols.add(col_idx)

        return list(rows), list(cols)

    def pushBomb(self, matrix, col_nums, row_nums):
        """

        :param matrix:
        :param point:
        :return:
        """
        for col_num in col_nums:
            for row_idx, _ in enumerate(matrix):
                matrix[row_idx][col_num] = 0

        for row_num in row_nums:
            for col_idx, _ in enumerate(matrix[0]):
                matrix[row_num][col_idx] = 0

