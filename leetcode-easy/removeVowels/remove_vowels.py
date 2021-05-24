class Solution:
    def removeVowels(self, s: str) -> str:
        st=""
        for i in s:
            if i not in ("a","e","i","o","u"):
                st+=i
        return st
    
