class Solution:
    int_chars_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        digits_len = len(digits)
        if digits_len == 0:
            return []
        out = self.int_chars_map[digits[0]]
        if digits_len == 1:
            return  out
        for d in digits[1:]:
            tmp_out = []
            for o in out:
                for char in self.int_chars_map[d]:
                    tmp_out.append(o + char)
            out = tmp_out
        return out

