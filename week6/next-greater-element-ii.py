"""

Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element.
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number.
If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

https://leetcode.com/problems/next-greater-element-ii/

"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        O(N^2) / O(N)

        """

        search_space = [num for num in nums]
        next_greater_map = {}

        answer = []

        for num in nums:

            print(search_space)

            found = False
            for item in search_space:
                if num < item:
                    next_greater_map[num] = item
                    found = True
                    break

            if not found:
                next_greater_map[num] = -1

            search_space.append(search_space.pop(0))

            print(num, next_greater_map[num])

            answer.append(next_greater_map[num])

        return answer


def main():
    nums = [1, 2, 1]
    expected = [2, -1, 2]
    answer = Solution().nextGreaterElements(nums)
    print("nums={} \texpected={} \tanswer={} is {}".format(nums, expected, answer, expected == answer))

    nums = [5, 4, 3, 2, 1]
    expected = [-1, 5, 5, 5, 5]
    answer = Solution().nextGreaterElements(nums)
    print("nums={} \texpected={} \tanswer={} is {}".format(nums, expected, answer, expected == answer))

    nums = [1, 5, 3, 6, 8]
    expected = [5, 6, 6, 8, -1]
    answer = Solution().nextGreaterElements(nums)
    print("nums={} \texpected={} \tanswer={} is {}".format(nums, expected, answer, expected == answer))

    nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
    expected = [120, 11, 120, 120, 123, 123, -1, 100, 100, 100]
    answer = Solution().nextGreaterElements(nums)
    print("nums={} \texpected={} \tanswer={} is {}".format(nums, expected, answer, expected == answer))


main()
