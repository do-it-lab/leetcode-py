"""

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.



Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

0 <= A.length <= 40,000
0 <= A[i] < 40,000

https://leetcode.com/problems/minimum-increment-to-make-array-unique/

"""


class Solution(object):

    """

    Idea
     * 모든 수를 정렬한 다음 index 가 하나씩 증가 할 때 마다, 현재 값은 이전 값 보다 1이 커야만 한다.
     * 이전 값 보다 1 큰 수와 현재 값의 차이가 증가 해야 하는 값이다.

    복잡도
     * time complexity is ( O(N) + 정렬 )
     * space complexity is O(1)
    """

    def minIncrementForUnique(self, A):

        nums = sorted(A)
        previous_value = None
        increment = 0

        for curr_num in nums:

            if (previous_value is not None) and (previous_value >= curr_num):

                diff = (previous_value + 1) - curr_num

                print(previous_value, curr_num, diff)

                previous_value = curr_num + diff
                increment += diff

            else:
                previous_value = curr_num

        return increment


class SolutionTimeLimitExceeded(object):

    def __init__(self):
        self.prev = set()

    def minIncrementForUnique(self, A):

        nums = sorted(A)
        total_increment = 0
        for num in nums:

            num, increment = self.__incrementIfExist(num, 0)
            #print(num, increment)

            total_increment += increment

        return total_increment

    def __incrementIfExist(self, num, increment):

        if num in self.prev:
            num, increment = self.__incrementIfExist(num + 1, increment + 1)

        self.prev.add(num)
        return num, increment


    def minIncrementForUnique_fail(self, A):
        """
        Time Limit Exceeded

        :type A: List[int]
        :rtype: int
        """

        A = sorted(A)

        uniq = {}
        total = 0
        for curr in A:
            inc, result = self.add(0, curr, uniq)
            total = total + inc
            uniq[result] = 0
            uniq[curr] = 0

        return total

    def add(self, inc, curr, uniq):
        if curr in uniq:
            return self.add(inc + 1, curr + 1, uniq)
        else:
            return inc, curr


def main():

    testCases = [
        [1, 2, 2],
        [3, 2, 1, 2, 1, 7],
        [0, 0]
    ]

    for testCase in testCases:
        leastNumber = Solution().minIncrementForUnique(testCase)
        print(leastNumber, testCase)

main()