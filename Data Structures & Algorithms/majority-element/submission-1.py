class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = 0
        res = 0 

        for i in nums:
            if curr == 0:
                res = i
                curr+=1
            
            if i == res:
                curr+=1
            
            else:
                curr-=1
        
        return res


            
        