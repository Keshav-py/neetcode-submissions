class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,L,M,R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]

            i = L
            k = 0 #left
            j = 0 #right

            while k < len(left) and j < len(right):
                if left[k] <= right[j]:
                    arr[i] = left[k]
                    k+=1
                else:
                    arr[i] = right[j]
                    j+=1
                i+=1
            
            while k < len(left):
                arr[i] = left[k]
                k+=1
                i+=1
            while j < len(right):
                arr[i] = right[j]
                j+=1
                i+=1


        def MergeSort(arr,l,r):
            if l==r:
                return arr

            m = (l+r)//2

            MergeSort(arr,l,m)
            MergeSort(arr,m+1,r)

            merge(arr,l,m,r)

            return arr

        return MergeSort(nums,0,len(nums)-1)

        