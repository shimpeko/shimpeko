class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # save first item in "prefix"
        prefix = strs[0]
        # start iteration form 2nd item of the list
        for s in strs[1:]:
            # create tmp var for prefix
            tmp = ''
            # iterate each char of the prefix
            for i, c in enumerate(prefix):
                try:
                    if s[i] == c:
                        tmp = tmp + c
                    else:
                        break
                except IndexError:
                    break
            prefix = tmp
        return prefix
