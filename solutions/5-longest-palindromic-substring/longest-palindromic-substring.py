class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = '|' + '|'.join(s) + '|'
        result = (0, '')

        for center in range(len(l)):
            rad = 0

            while center - (rad + 1) >= 0 and \
                    center + (rad + 1) < len(l) and \
                    l[center - (rad+1)] == l[center + (rad+1)]:
                rad += 1

            if result[0] < rad:
                result = (rad, l[center - rad: center + rad + 1])

        return ''.join(result[1].split('|'))


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
