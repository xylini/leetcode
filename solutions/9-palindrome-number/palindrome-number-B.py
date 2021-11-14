class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x is negative or number end with 0 then cannot be palindrome
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        y = 0

        while x > y:
            x, y = x // 10, y * 10 + x % 10

        return x == y or x == y // 10


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
