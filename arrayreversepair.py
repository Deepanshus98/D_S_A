class Solution:
    def reversePairs(self, nums):
        if not nums:
            return 0
        return merge_and_count(nums, 0, len(nums)-1)
        
def merge_and_count(nums, start, end):
    if start >= end:
        return 0
    count = 0
    mid = (start+end)//2
    count += merge_and_count(nums, start, mid)
    count += merge_and_count(nums, mid+1, end)
    
    left = start
    right = mid + 1
    while left<=mid and right<=end:
        if nums[left] > 2 * nums[right]:
            count += mid - left + 1
            right += 1
        else:
            left +=1
    nums[start:end+1] = sorted(nums[start:end+1])
    return count


      