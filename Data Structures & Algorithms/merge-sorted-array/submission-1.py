class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = (m+n)-1

        n2 = n-1

        m1 = m-1


        while n2 >= 0 and i>=0:

            if m1>=0 and nums1[m1] > nums2[n2]:

                nums1[i],nums1[m1] = nums1[m1],nums1[i]

                m1 -= 1

            elif m1>=0 and nums1[m1] < nums2[n2]:

                nums1[i] = nums2[n2]

                n2 -= 1
            
            else:
                nums1[i] = nums2[n2]
                n2 -= 1
            
            i -= 1
        
        return nums1
            









        



        