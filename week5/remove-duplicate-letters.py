"""

316. Remove Duplicate Letters

Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

bcabc
 - bca
 - abc

bcac
cabc

Input: "cbacdcbc"
Output: "acdb"

cbad
bacd


Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

https://leetcode.com/problems/remove-duplicate-letters/

"""


class Solution(object):

    def removeDuplicateLetters(self, s):
        """

        일단 쌓아,
        중복 나왔어
        바로 뒤에 값 있으면, 한번 봐, 중복 아닐 때 까지 계속 포함해,
        그거랑 함께 해서, 앞에꺼 지우는거랑 뒤에꺼 지우는 거와 어느게 더 작은지 비교해,
        중복을 삭제해,
        마지막 문자까지

        :type s: str
        :rtype: str
        """
        answer = []

        for idx, letter in enumerate(s):
            if answer and letter in answer:

                # check next_letter -> candidate and remove_letter
                if idx+1 < len(s):
                    next_letter = s[idx+1]

                # compare

                #




            answer.append(letter)
