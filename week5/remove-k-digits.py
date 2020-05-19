"""

402. Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""

import time


class Solution(object):
    """
    O(N)/O(N)
    """

    def __init__(self):
        self.debug = False
        self.stack = None
        self.possible_remove_count = 0

    def removeKdigits(self, num, k):

        self.stack = MyStack()
        self.possible_remove_count = k

        for letter in num:
            self.removeBiggerThan(letter)
            self.stack.push(letter)

            if self.debug:
                print("{}".format(self.stack.to_string()))
                time.sleep(0.5)

        return self.removeLeadingZero(self.removeTail(self.stack.to_string()))

    def removeBiggerThan(self, letter):

        if not self.stack.isEmpty() \
                and self.stack.peek() > letter \
                and self.possible_remove_count:

            self.stack.pop()
            self.possible_remove_count = self.possible_remove_count - 1
            self.removeBiggerThan(letter)

    def removeTail(self, num):
        if self.possible_remove_count:
            return num[:-self.possible_remove_count]
        else:
            return num

    def removeLeadingZero(self, num):
        if num:
            if num[0] == '0':
                return self.removeLeadingZero(num[1:])
            else:
                return num
        else:
            return "0"


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
    num = "1432219"
    k = 3

    answer = Solution().removeKdigits(num, k)
    expected = "1219"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "10200"
    k = 1

    answer = Solution().removeKdigits(num, k)
    expected = "200"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "10"
    k = 2

    answer = Solution().removeKdigits(num, k)
    expected = "0"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "112"
    k = 1

    answer = Solution().removeKdigits(num, k)
    expected = "11"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "110"
    k = 1

    answer = Solution().removeKdigits(num, k)
    expected = "10"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "1173"
    k = 2

    answer = Solution().removeKdigits(num, k)
    expected = "11"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "5337"
    k = 2

    answer = Solution().removeKdigits(num, k)
    expected = "33"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "43214321"
    k = 4

    answer = Solution().removeKdigits(num, k)
    expected = "1321"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))

    num = "9"
    k = 1

    answer = Solution().removeKdigits(num, k)
    expected = "0"
    print("num={}, k={}, answer={}, expected={}, {}".format(num, k, answer, expected, answer == expected))


main()
