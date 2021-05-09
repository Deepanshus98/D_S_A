# An efficient Python program to 
# count distinct elements in 
# every window of size k 
from collections import defaultdict 
  
def countDistinct(arr, k, n): 
  
    # Creates an empty hashmap hm  
    mp = defaultdict(lambda:0) 
  
    # initialize distinct element  
    # count for current window  
    dist_count = 0
  
    # Traverse the first window and store count  
    # of every element in hash map  
    for i in range(k): 
        if mp[arr[i]] == 0: 
            dist_count += 1
        mp[arr[i]] += 1
  
    # Print count of first window  
    print(dist_count) 
      
    # Traverse through the remaining array  
    for i in range(k, n): 
  
        # Remove first element of previous window  
        # If there was only one occurrence,  
        # then reduce distinct count.  
        if mp[arr[i - k]] == 1: 
            dist_count -= 1
        mp[arr[i - k]] -= 1
      
    # Add new element of current window  
    # If this element appears first time,  
    # increment distinct element count  
        if mp[arr[i]] == 0: 
            dist_count += 1
        mp[arr[i]] += 1
  
        # Print count of current window  
        print(dist_count) 
  
arr = [1, 2, 1, 3, 4, 2, 3] 
n = len(arr) 
k = 4
countDistinct(arr, k, n) 
