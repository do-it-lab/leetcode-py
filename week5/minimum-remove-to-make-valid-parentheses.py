"""

1249. Minimum Remove to Make Valid Parentheses
Medium

582

21

Add to List

Share
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.

"""


class Solution(object):
    """
    O(N)/O(N)
    """

    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        invalid_indices = self.findIndicesOfInvalidParentheses(s)
        answer = self.extractStringWithValidParentheses(s, invalid_indices)

        return answer

    def findIndicesOfInvalidParentheses(self, s):

        OPEN, CLOSE, EXIST_FLAG = '(', ')', 1

        invalid_indices = {}
        open_parentheses = MyStack()

        for index, letter in enumerate(s):

            if letter == OPEN:

                open_parentheses.push(index)
                invalid_indices[index] = EXIST_FLAG

            elif letter == CLOSE:

                if not open_parentheses.isEmpty():
                    open_index = open_parentheses.pop()
                    del invalid_indices[open_index]

                else:
                    invalid_indices[index] = EXIST_FLAG

        return invalid_indices

    def extractStringWithValidParentheses(self, s, invalid_indices):

        result_string = []
        for index, letter in enumerate(s):
            if index not in invalid_indices:
                result_string.append(letter)

        return "".join(result_string)


class MyStack(object):

    def __init__(self):
        self.store = []

    def push(self, element):
        self.store.append(element)

    def peek(self):
        return self.store[-1]

    def pop(self):
        head = self.store[-1]
        del self.store[-1]
        return head

    def to_string(self):
        return "".join(self.store)

    def isEmpty(self):
        return len(self.store) == 0


class Solution1(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        invalid_idx = {}
        left = []

        for idx, letter in enumerate(s):
            if letter == ')':

                if left:
                    left_idx = left.pop()
                    del invalid_idx[left_idx]

                else:
                    invalid_idx[idx] = 1

            elif letter == '(':

                invalid_idx[idx] = 1
                left.append(idx)

        return "".join([letter if idx not in invalid_idx else "" for idx, letter in enumerate(s)])


def main():

    s = "lee(t(c)o)de)"
    expected = "lee(t(c)o)de"
    answer = Solution().minRemoveToMakeValid(s)
    print(s, expected, answer, expected == answer)

    s = "a)b(c)d"
    expected = "ab(c)d"

    answer = Solution().minRemoveToMakeValid(s)
    print(s, expected, answer, expected == answer)

    s = "))(("
    expected = ""

    answer = Solution().minRemoveToMakeValid(s)
    print(s, expected, answer, expected == answer)

main()