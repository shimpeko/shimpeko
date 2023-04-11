class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_minus = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            is_minus = True
        temp_dividend = ''
        answer = ''
        abs_divisor = abs(divisor)
        for n in str(abs(dividend)):
            temp_dividend = int(str(temp_dividend) + n)
            if temp_dividend>= abs_divisor:
                temp_answer = 0
                while True:
                    temp_answer = temp_answer + 1
                    temp_dividend = temp_dividend - abs_divisor
                    if temp_dividend < abs_divisor:
                        break
                answer = answer + str(temp_answer)
            else:
                answer = answer + '0'
        if is_minus:
            answer = '-' + answer
        int_max = 2**31
        answer = int(answer)
        if answer >= (int_max- 1):
            return int_max - 1
        elif answer <= (-int_max):
            return -int_max
        return answer
