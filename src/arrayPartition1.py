class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here

        return sum(sorted(nums)[::2])

