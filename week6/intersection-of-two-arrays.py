"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

https://leetcode.com/problems/intersection-of-two-arrays/

"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        uniq_nums1, uniq_nums2 = set(nums1), set(nums2)

        if len(uniq_nums1) < len(uniq_nums2):
            smaller = uniq_nums1
            bigger = uniq_nums2
        else:
            smaller = uniq_nums2
            bigger = uniq_nums1

        return [item for item in list(smaller) if item in bigger]


