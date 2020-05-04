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

https://leetcode.com/problems/increasing-triplet-subsequence/

"""


class Solution(object):
    """

    접근
     * i, j, k 값이 변함에 따라 첫번째 값, 두번째 값, 세번째 값이 존재한다.
     * 첫번째 보다 크고, 두번째 보다 큰, 세번째 값이 존재한다면 True 다
     * 1) 첫번째 값은 처음에 설정한 다음, 언제 바꿔야 할까?
     * 2) 처음 두번째 값은, 첫번째 값(Left)보다 큰 값이 나올 경우에 설정해준다. 그 다음 언제 바꿔야 할까?

    해결
     * 1) 현재 Num 값이 더 작을 경우 바꿔 준다.
        - 값이 같은 경우는 처리를 하지 않는다.
        - Second 가 존재하므로, First 는 더 낮아져도 상관이 없고, 오른쪽에 있는 값들과 비교 하기 위해 first를 변경한다

     * 2) 현재 Num 값 First 보다 크고 Second 보다 작을 때 바꿔 준다 (같은 경우는 무시)
        - 오른쪽에 있는 나머지 값들과 비교 하기 위해 second 를 변경한다

    """

    def increasingTriplet(self, nums):

        first = float('inf')
        second = float('inf')

        for num in nums:
            print(first, second)
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False

    def increasingTripletMyFirstSolution(self, nums):

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

    testcase = [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 3]

    result = Solution().increasingTriplet(testcase)
    print(result)

    result = Solution().increasingTripletMyFirstSolution(testcase)
    print(result)


main()
