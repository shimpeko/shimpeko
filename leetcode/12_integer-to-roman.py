class Solution:

    i_r = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    def intToRoman(self, num: int) -> str:
        out = ''
        for idx, s in enumerate(str(num)[::-1]):
            target_int = int(s)
            item = Solution.i_r.get(10**idx * target_int)
            if item:
                out = item + out
                continue
            if target_int >= 5:
                x = target_int - 5
                out = (Solution.i_r.get(10**idx) * x) + out
                out = Solution.i_r.get(5 * (10**idx)) + out
            else:
                out = (Solution.i_r.get(10**idx) * target_int) + out
        return out
