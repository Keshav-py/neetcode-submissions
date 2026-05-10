class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i,n in enumerate(nums):
            need = target - n
            if need in hmap.keys():
                return [hmap[need],i]
            hmap[n] = i



        