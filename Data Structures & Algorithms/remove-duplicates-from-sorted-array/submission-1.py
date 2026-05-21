class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        curr = nums[0]

        for i in range(1,len(nums)):
            if curr == nums[i] :
                nums[i] = "#"
            
            else:
                curr = nums[i]
            
        
        k = 0

        for i in range(len(nums)):

            if nums[i] != "#":
               nums[k]=nums[i] 
               k+=1
            else:
                continue
            
        
        return k





        