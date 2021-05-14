class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        q = collections.deque()
        q.append(0)
        for i in range(1,k-1):
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
        ans = []
        for i in range(k-1,n):
            if q[0] == i-k:
                q.popleft()
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans
