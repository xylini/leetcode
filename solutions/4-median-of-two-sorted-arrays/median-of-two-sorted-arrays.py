from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        i_l, i_h = 0, m
        mid = (m + n + 1) // 2

        while i_l <= i_h:
            i = (i_l + i_h) // 2
            j = mid - i

            if i > 0 and nums1[i - 1] > nums2[j]:
                i_h = i
            elif i < m and nums2[j - 1] > nums1[i]:
                i_l = i + 1
            else:
                if i == 0:
                    ml = nums2[j - 1]
                elif j == 0:
                    ml = nums1[i - 1]
                else:
                    ml = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return ml

                if i == m:
                    mr = nums2[j]
                elif j == n:
                    mr = nums1[i]
                else:
                    mr = min(nums1[i], nums2[j])

                return (ml + mr) / 2


def main():
    testCases = [(
        [1, 3],
        [2]
    ), (
        [1, 2],
        [3, 4]
    ), (
        [0, 0],
        [0, 0]
    ), (
        [],
        [1]
    ), (
        [2],
        []
    )]

    for test in testCases:
        print(Solution().findMedianSortedArrays(*test))


if __name__ == '__main__':
    main()