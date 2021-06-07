class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr = {}
        start = 0

        for stop, val in enumerate(s):
            if val in curr:
                start = max(start, curr[val] + 1)
            curr[val] = stop
            max_len = max(max_len, stop - start + 1)

        return max_len


def main():
    testCases = [
        'abcabcbb',
        'bbbbb',
        'pwwkew',
        ''
    ]

    for test in testCases:
        print(Solution().lengthOfLongestSubstring(test))


if __name__ == '__main__':
    main()
