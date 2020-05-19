"""

1047. Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.

"""


class Solution(object):
    """
    O(N)/O(N)
    """

    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """

        stack = MyStack()

        for letter in S:
            if stack.isEmpty():
                stack.push(letter)
            elif stack.peek() == letter:
                stack.pop()
            else:
                stack.push(letter)
        return stack.to_string()


class MyStack(object):

    def __init__(self):
        self.store = []

    def push(self, element):
        self.store.append(element)

    def peek(self):
        return self.store[-1]

    def pop(self):
        del self.store[-1]

    def to_string(self):
        return "".join(self.store)

    def isEmpty(self):
        return len(self.store) == 0

def main():
    S = "abbaca"
    answer = Solution().removeDuplicates(S)
    print(answer)

main()