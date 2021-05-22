class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr, cur = [], head
        while cur:  # linked list -> array
            arr.append(cur.val)
            cur = cur.next  # go ahead
        return arr == arr[::-1]#comparing it with reversed order and return if its true else false
