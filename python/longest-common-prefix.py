#longest common prefix
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str=""
        m=min(len(w)for w in strs)
        for i in range(m):
            current=strs[0][i]
            if all(current==word[i] for word in strs):
                str+=strs[0][i]
            else:
                break
        return str
