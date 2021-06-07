from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i, v in enumerate(nums):
            k = target - v
            if k not in a:
                a[v] = i
            else:
                return [a[k], i]


def main():
    testCases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6,),
        ([3, 3], 6)
    ]

    for test in testCases:
        print(Solution().twoSum(*test))


if __name__ == '__main__':
    main()
