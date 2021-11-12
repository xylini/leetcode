# Pythonic solution which iterates through rows, slicing, zipping and concatenating the input string

def merge_to_single_string(first, second) -> str:
    if len(first) > len(second):
        a, b, c = first[:len(second)], second, first[len(second):]
    else:
        a, b, c = first, second[:len(first)], second[len(first):]

    zipped = ''.join([''.join(letter) for letter in list(zip(a, b))])

    return zipped + c


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # const shift between letters in rows
        k = (numRows - 2) * 2 + 2

        # case 1 - one row
        if numRows == 1:
            return s

        # case 2 - top, middle (which may be 0 when numRows == 2) and bottom
        top = s[0::k]
        middle = ''.join([merge_to_single_string(s[i::k], s[k - i::k]) for i in range(1, numRows - 1)])
        bottom = s[numRows - 1::k]

        return top + middle + bottom


def main():
    testCases = [
        ('PAYPALISHIRING', 3),
        ('PAYPALISHIRING', 4),
        ('A', 1)
    ]

    for test in testCases:
        print(Solution().convert(*test))


if __name__ == '__main__':
    main()
