class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        longest = 0
        length = 0

        for i in nums:
            if (i-1) not in numset:
                while (i+length) in numset:
                    length+=1
                longest = max(longest,length)
                length = 0
        
        return longest


        