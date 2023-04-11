class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        needle_len = len(needle)
        haystack_len = len(haystack)
        for n in range(haystack_len):
            if haystack[n: n + needle_len] == needle:
                return n
        return -1
