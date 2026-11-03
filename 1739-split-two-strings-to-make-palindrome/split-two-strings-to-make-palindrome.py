class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        #Function
        def isPall(s,i,j):
            while i < j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True 

        def check(a,b):
            i = 0
            j = len(a)-1
            while i < j:
                if a[i] == b[j]:
                    i+=1
                    j-=1
                else:
                    return isPall(a,i,j) or isPall(b,i,j)
            return True            

        return check(a,b) or check(b,a)                              


        