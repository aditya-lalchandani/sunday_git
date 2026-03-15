class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max, starting, characters = 0, 0, {}
        for i in range(len(s)):
            if s[i] in characters and starting <= characters[s[i]]: starting = characters[s[i]] + 1
            else: max = max(max, i - starting + 1)
            characters[s[i]] = i
        return max