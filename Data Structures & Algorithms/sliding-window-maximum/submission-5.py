class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        retList = []

        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > 0 and l-1 == q[0]:
                q.popleft()

            if r == l+k-1:
                retList.append(nums[q[0]])
                l += 1
            r += 1

        return retList

            

        ###############

        retList = []

        l = 0
        r = k
        while r <= len(nums):
            retList.append(max(nums[l:r]))
            l += 1
            r += 1

        return retList