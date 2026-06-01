class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        retList = []

        left = 0
        right = len(nums)-1

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            prev = [-1,-1,-1]
            while l < r:
                sum1 = nums[i] + nums[l] + nums[r]
                curr = [nums[i], nums[l], nums[r]]
                if sum1 == 0 and curr != prev:
                    retList.append(curr)
                    prev = curr
                    l += 1
                    r -= 1
                elif sum1 < 0:
                    l += 1
                elif sum1 > 0:
                    r -= 1
                else:
                    l += 1
                    r -= 1


        return retList



# [-1,-1,0,1,2,4]





