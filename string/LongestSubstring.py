# -*- coding: utf-8 -*
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxlength = start = 0
    used = {}
    for i in range(len(s)):
        if s[i] in used and start <= used[s[i]]:
            start = used[s[i]] + 1
        else:
            maxlength = max(maxlength, i - start + 1)
        used[s[i]] = i

    return maxlength


res = lengthOfLongestSubstring("abcabcbb")
print(res)