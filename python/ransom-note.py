#ransom note
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lr=list(ransomNote)
        lm=list(magazine)
        if len(lr)<=len(lm):
            for i in lr:
                if i in lm:
                    lm.remove(i)
                else:
                    return False
        else:
            return False

        return True
