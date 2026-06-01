class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        retVal = [-1, -1]

        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                retVal[0] = mid
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid+1

        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] == target:
                retVal[1] = mid
                left = mid+1
            elif nums[mid] > target:
                right = mid
            else:
                left = mid+1

        return retVal
            

        