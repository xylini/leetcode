class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = -int(str(x)[1:][::-1])
        else:
            result = int(str(x)[::-1])

        limit = 2147483648

        return result if -limit <= result <= limit - 1 else 0


def main():
    testCases = [
        123,
        -123,
        120,
        0
    ]

    for test in testCases:
        print(Solution().reverse(test))


if __name__ == '__main__':
    main()
