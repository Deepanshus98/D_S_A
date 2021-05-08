from collections import defaultdict
def subarrayXor(arr, n, m): 
    HashTable=defaultdict(bool)
    HashTable[0]=1
    count=0
    curSum=0
    for i in arr:
        curSum^=i
        if HashTable[curSum^m]:
            count+=HashTable[curSum^m]
        HashTable[curSum]+=1
    return(count)
         
 
# Driver program to test above function 
def main(): 
    arr = [ 5, 6, 7, 8, 9 ] 
    n = len(arr) 
    m = 5
 
    print("Number of subarrays having given XOR is "
        , subarrayXor(arr, n, m)) 
 
if __name__ == '__main__': 
    main() 
