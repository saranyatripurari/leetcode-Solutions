class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        digit_sum = 0

        while temp:
            digit = temp % 10
            digit_sum += digit
            temp //= 10

        if x % digit_sum == 0:
            return digit_sum

        return -1