"""


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?



Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28


Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^

https://leetcode.com/problems/unique-paths/


"""


class Solution(object):

    def __init__(self):
        self.memo = dict()
        self.target_pos = (0, 0)

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        self.target_pos = (m, n)

        for x in range(1, m+1):
            for y in range(1, n+1):
                num_of_paths = self.findUniquePaths(x, y)
                self.saveMemo(curr_pos=(x, y), num_of_paths=num_of_paths)

        return num_of_paths

    def findUniquePaths(self, x, y):

        paths = 0
        if self.hasOnlyOnePath(x, y):
            paths = 1
        elif self.hasKnownPaths(x, y):
            paths = self.getPaths(x, y)
        else:
            print("error", x, y)
            exit(1)
        return paths

    def saveMemo(self, curr_pos, num_of_paths):
        self.memo[curr_pos] = num_of_paths
        self.memo[(curr_pos[1], curr_pos[0])] = num_of_paths

    def hasOnlyOnePath(self, x, y):
        return x == 1 or y == 1

    def hasKnownPaths(self, x, y):
        return ((x, y-1) in self.memo or (y-1, x) in self.memo)\
               and ((x-1, y) in self.memo or (y, x-1) in self.memo)

    def getPaths(self, x, y):
        from_top_paths = self.memo[(x, y-1)]
        from_left_paths = self.memo[(x-1, y)]

        return from_top_paths + from_left_paths


class SolutionSecond(object):

    def __init__(self):
        self.memo = dict()

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        val = 0

        for x in range(1, m + 1):
            for y in range(1, n + 1):
                val = self.calc(x, y)
                print("x={}, y={}, val={}".format(x, y, val))
                self.add(x, y, val)
        return val

    def add(self, x, y, val):
        self.memo[(x, y)] = val
        self.memo[(y, x)] = val

    def calc(self, x, y):

        if x == 1 or y == 1:
            return 1

        if x == y:

            if y - 1 == 1:
                return 1 * 2
            else:
                return self.memo[(x, y - 1)] * 2
        else:

            left = self.memo[(x, y - 1)] if y - 1 != 1 else 1
            right = self.memo[(x - 1, y)] if x - 1 != 1 else 1

            return left + right


class SolutionByRecurrsion(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


def main():
    m, n = 3, 2
    print(Solution().uniquePaths(m, n))
    #print(SolutionSecond().uniquePaths(m, n))
    #print(SolutionByRecurrsion().uniquePaths(m, n))


main()
