class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x >= 0 covers edge case, because when x is negative it cannot be palindrome
        return x >= 0 and str(x) == str(x)[::-1]


def main():
    testCases = [
        121,
        -121,
        10,
        -101
    ]

    for test in testCases:
        print(Solution().isPalindrome(test))


if __name__ == '__main__':
    main()
