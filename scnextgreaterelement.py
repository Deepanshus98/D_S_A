class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev_l = len(nums)
        nums = nums+nums
        stack = []
        ans = [-1]*len(nums)
        for i, n in enumerate(nums):
            while stack and stack[-1][1] < n:
                prev_i = stack.pop()[0]
                ans[prev_i] = n
            stack.append([i, n])
            
        return ans[:prev_l]
