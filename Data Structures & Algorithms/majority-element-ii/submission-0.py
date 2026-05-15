class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = {}
        res = []
        for i in nums:
            hmap[i] = 1+hmap.get(i,0)
        
        for k,v in hmap.items():
            if v > (len(nums)/3):
                res.append(k)
        
        return res
        

        