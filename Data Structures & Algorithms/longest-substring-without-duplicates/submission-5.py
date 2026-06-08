class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        hmap = set()
        maxl = 0

        for r in range(len(s)):

            while s[r] in hmap:
                hmap.remove(s[l])
                l+=1
            
            hmap.add(s[r])
            maxl = max(maxl,r-l+1)
        return maxl



            
            


        