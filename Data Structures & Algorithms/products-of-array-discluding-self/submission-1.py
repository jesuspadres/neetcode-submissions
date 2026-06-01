class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1 = [1 for n in nums]
        list2 = [1 for n in nums]

        for i in range(len(list1)-2, -1, -1):
            list1[i] = list1[i+1] * nums[i+1]

        for i in range(1, len(list2)):
            list2[i] = list2[i-1] * nums[i-1]

        retList = []
        print(list1)
        print(list2)

        for i in range(len(nums)):
            retList.append(list1[i] * list2[i])


        return retList


