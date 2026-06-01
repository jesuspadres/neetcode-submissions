class Solution:
    def findMin(self, nums: List[int]) -> int:
        retVal = nums[0]

        l = 0
        r = len(nums)
        

        while l < r:
            mid = (l+r)//2
            retVal = min(nums[l], nums[r-1], nums[mid], retVal)

            if nums[r-1] > nums[mid]:
                r = mid
            else:
                l = mid+1

        return retVal
