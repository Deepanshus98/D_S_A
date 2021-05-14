class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        w_list = []
        for eve_w in s.split(" "):
            if eve_w:
                w_list.append(eve_w)
        return " ".join(reversed(w_list))
