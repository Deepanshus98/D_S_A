# Python 3 program to count  
# maximum consecutive 1's  
# in a binary array. 
  
# Returns count of maximum  
# consecutive 1's in binary 
# array arr[0..n-1] 
def getMaxLength(arr, n): 
  
    # intitialize count 
    count = 0 
      
    # initialize max 
    result = 0 
  
    for i in range(0, n): 
      
        # Reset count when 0 is found 
        if (arr[i] == 0): 
            count = 0
  
        # If 1 is found, increment count 
        # and update result if count  
        # becomes more. 
        else: 
              
            # increase count 
            count+= 1 
            result = max(result, count)  
          
    return result  
  
# Driver code 
arr = [1, 1, 0, 0, 1, 0, 1,  
             0, 1, 1, 1, 1]  
n = len(arr)  
  
print(getMaxLength(arr, n)) 
  
# This code is contributed by Smitha Dinesh Semwal 
