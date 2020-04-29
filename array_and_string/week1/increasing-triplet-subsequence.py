"""

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false


"""
import bisect


class Solution(object):

    def increasingTriplet(self, nums):

        first = float('inf')
        second = float('inf')

        for num in nums:
            if num < first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

    def increasingTripletFirstSolution(self, nums):


        candidates = []
        isExist = False

        for num in nums:

            print(candidates, num)
            if not candidates:
                candidates.append(num)

            elif len(candidates) == 1:
                if candidates[0] < num:
                    candidates.append(num)
                else:
                    candidates[0] = num

            else:
                print(candidates)
                check = list(candidates)
                check.append(num)
                isExist, result = self.isExist(check)
                candidates = result

                if isExist:
                    break

        return isExist

    def isExist(self, candidates):

        print(candidates)

        if candidates[0] < candidates[1] < candidates[2]:
            return True, None
        elif candidates[2] < candidates[0]:
            return False, [candidates[2]]
        elif candidates[0] < candidates[2] < candidates[1]:
            return False, [candidates[0], candidates[2]]
        else:
            return False, candidates[:2]



def main():
    my = [1, 0, 2, 0, -1, 3]
    result = Solution().increasingTriplet(my)
    print(result)

    result = Solution().bestSolution(my)
    print(result)


main()