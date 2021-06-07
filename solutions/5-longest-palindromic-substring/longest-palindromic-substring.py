class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = '|' + '|'.join(s) + '|'
        results = []

        for center in range(len(l)):
            rad = 0

            while center - (rad + 1) >= 0 and \
                    center + (rad + 1) < len(l) and \
                    l[center - (rad+1)] == l[center + (rad+1)]:
                rad += 1

            results.append(rad)

        m = max(results)
        return m


def main():
    testCases = [
        'babad',
        'cbbd',
        'a',
        'ac',
        'bbbb'
    ]

    for test in testCases:
        print(Solution().longestPalindrome(test))


if __name__ == '__main__':
    main()
