"""

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int

        시간 제한 초과

        """

        return self.findMaxArea(self.transform(height))

    def transform(self, height):
        return [(x, y) for x, y in enumerate(height)]

    def findMaxArea(self, points):

        maxValue = 0

        for idx, leftA in enumerate(points):
            for rightA in points[idx:]:
                value = self.area(leftA, rightA)

                if maxValue < value:
                    maxValue = value

        return maxValue

    def area(self, leftA, rightA):

        (x1, y1) = leftA
        (x2, y2) = rightA

        if y1 < y2:
            yt = y1
        else:
            yt = y2

        width = abs(x2 - x1)
        height = abs(yt - 0)

        return width * height


def main():

    sample = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    maxArea = Solution().maxArea(height=sample)

    print(maxArea)

main()
