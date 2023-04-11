class Solution:
    brackets = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    def isValid(self, s: str) -> bool:
        # temp open bracket 
        open_brackets = []
        # loop each char in s
        for b in s:
            if b in Solution.brackets.values():
                open_brackets.append(b)
                continue
            # evaluate under here only if b is not open bracket
            if not open_brackets:
                return False
            last_bracket = open_brackets.pop()
            if last_bracket == Solution.brackets[b]:
                continue
            else:
                return False
        if open_brackets:
            return False
        return True