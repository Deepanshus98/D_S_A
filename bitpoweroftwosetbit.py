# Python3 Program to find 
# whether a no is 
# power of two
import math
class Solution(object):
    def Log2(self, x):
        if x == 0:
            return false
 
        return (math.log10(x) / math.log10(2))
 
# Function to check
# if x is power of 2
    def isPowerOfTwo(self, n):
        return (math.ceil(self.Log2(n)) == math.floor(self.Log2(n)))
        """
        :type n: int
        :rtype: bool
        """
        
 
# Driver Code
if(isPowerOfTwo(31)):
    print("Yes");
else:
    print("No");
 
if(isPowerOfTwo(64)):
    print("Yes");
else:
    print("No");
