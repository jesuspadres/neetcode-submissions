class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def helper(left, right):
            if (right - left) < 2:
                return nums[left:right]

            mid = (left + right) // 2

            leftArr = helper(left, mid)
            rightArr = helper(mid, right)

            nI = left
            lI = rI = 0

            while nI < right:
                if lI >= len(leftArr):
                    nums[nI] = rightArr[rI]
                    rI += 1
                elif rI >= len(rightArr):
                    nums[nI] = leftArr[lI]
                    lI += 1
                else:
                    if leftArr[lI] <= rightArr[rI]:
                        nums[nI] = leftArr[lI]
                        lI += 1
                    else:
                        nums[nI] = rightArr[rI]
                        rI += 1
                nI += 1

            return nums[left:right]

        helper(0, len(nums))

        return nums