#valid parenthesis
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        match={'(':')','[':']','{':'}'}
        if len(s)<=1:
            return False
        for p in s:
            if p in '([{':
                st.append(p)
            else:
                if not st or match[st[-1]]!=p:
                    return False
                st.pop()
        return len(st)==0
