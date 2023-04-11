class Solution:
    symbols_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        number = 0
        max_idx = len(s) - 1
        for i, c in enumerate(s):
            n = Solution.symbols_to_int[c]
            if max_idx > i and n < Solution.symbols_to_int[s[i+1]]:
                number = number - n
            else:
                number = number + n
        return number
