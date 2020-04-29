class Solution(object):

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

    A = [3, 2, 1, 2, 1, 7]

    leastNumber = Solution().minIncrementForUnique(A)

    print(leastNumber)

main()