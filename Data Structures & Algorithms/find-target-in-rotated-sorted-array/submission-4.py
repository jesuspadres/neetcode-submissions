class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif (nums[mid] < target and nums[r-1] >= target) or (nums[mid] > target and nums[r-1] >= target and nums[r-1] < nums[mid]):
                l = mid+1
            else:
                r = mid

        return -1