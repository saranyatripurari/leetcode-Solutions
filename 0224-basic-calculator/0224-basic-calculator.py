class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for ch in s:

            # Build the number
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Add the current number
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1

            # Subtract the current number
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1

            # Start a new bracket
            elif ch == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            # Close the bracket
            elif ch == ')':
                result += sign * num
                num = 0

                sign = stack.pop()
                previous_result = stack.pop()

                result = previous_result + sign * result

        # Add the last number
        result += sign * num

        return result