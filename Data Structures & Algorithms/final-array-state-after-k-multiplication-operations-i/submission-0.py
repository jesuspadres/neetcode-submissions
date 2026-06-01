class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            minIdx = 0
            for i in range(len(nums)):
                if nums[i] < nums[minIdx]:
                    minIdx = i
            
            nums[minIdx] *= multiplier

        return nums