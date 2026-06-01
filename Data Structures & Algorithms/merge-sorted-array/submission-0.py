class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        sortedIdx = -1
        index1 = -1 - n
        index2 = -1

        while sortedIdx >= -len(nums1):
            if index2 < -n:
                nums1[sortedIdx] = nums1[index1]
                index1 -= 1
            elif index1 < -len(nums1):
                nums1[sortedIdx] = nums2[index2]
                index2 -= 1
            elif nums1[index1] >= nums2[index2]:
                nums1[sortedIdx] = nums1[index1]
                index1 -= 1
            else:
                nums1[sortedIdx] = nums2[index2]
                index2 -= 1
            sortedIdx -= 1

        
            
        