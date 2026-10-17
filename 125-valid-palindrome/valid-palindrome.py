class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = ""
        temp = ""
        temp2 = ""

        for ch in s:
            if ch.isalnum():
                res += ch
            temp = res.lower()


        l= 0
        r= len(temp) - 1
        while l < r:
            if temp[l] != temp[r]:
                return False
            l+=1
            r-=1
        return True


        