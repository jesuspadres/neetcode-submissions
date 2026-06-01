class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = 0
        product = 1

        while right < len(nums):
            product *= nums[right]
            print(product, left, right)

            if product < k:
                count += right - left + 1
                right += 1
            else:
                product = max(1, product // nums[left] // nums[right])
                left += 1

            if left > right:
                right = left

        return count
        