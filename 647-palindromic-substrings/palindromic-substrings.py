class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand(s,l,r):
            count = 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 1
                    l-=1
                    r+=1
                else:
                    break  
            return count
        
        n = len(s)
        ans = 0
        for i in range(n):
            ans += expand(s,i,i) #odd
            ans += expand(s,i,i+1) #even
        return ans    
        
        