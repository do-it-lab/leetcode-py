"""

224. Basic Calculator
Hard

1328

121

Add to List

Share
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

https://leetcode.com/problems/basic-calculator/

"""


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # operator and operand and eval
        operator = None
        operands = []
        for term in s:
            if term == ' ':
                continue

            if '+' == term:
                operator = '+'
            elif '-' == term:
                operator = '-'
            else:
                operands.append(term)

        return self.eval(operator, operands)

    def eval_expression(self, expression):
        if '(' not in expression:
            return int(expression)

    def eval(self, operator, operands):

        if operator == '+':
            return self.eval_expression(operands[0]) + self.eval_expression(operands[1])
        elif operator == '-':
            return self.eval_expression(operands[0]) - self.eval_expression(operands[1])


def main():
    s = "1 + 1"
    expected = 2
    answer = Solution().calculate(s)
    print("{}={}/ my answer={} is {}", s, expected, answer, expected == answer)

    s = " 2-1 + 2 "
    expected = 3
    answer = Solution().calculate(s)
    print("{}={}/ my answer={} is {}", s, expected, answer, expected == answer)

    s = "(1+(4+5+2)-3)+(6+8)"
    expected = 23
    answer = Solution().calculate(s)
    print("{}={}/ my answer={} is {}", s, expected, answer, expected == answer)


main()