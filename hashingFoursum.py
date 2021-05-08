# Function to check if quadruplet exists in a list with the given sum
def quadTuple(A, n, sum):
 
    # create an empty dictionary
    # `key` —> sum of a pair in the list
    # `value` —> list storing an index of every pair having that sum
    dict = {}
 
    # consider each element except the last element
    for i in range(n - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, n):
 
            # calculate the remaining sum
            val = sum - (A[i] + A[j])
 
            # if the remaining sum is found on the dictionary,
            # we have found a quadruplet
            if val in dict:
 
                # check every pair having a sum equal to the remaining sum
                for pair in dict[val]:
                    x, y = pair
 
                    # if quadruplet doesn't overlap, print it and return true
                    if (x != i and x != j) and (y != i and y != j):
                        print("Quadruplet Found", (A[i], A[j], A[x], A[y]))
                        return True
 
            # insert the current pair into the dictionary
            dict.setdefault(A[i] + A[j], []).append((i, j))
 
    # return false if quadruplet doesn't exist
    return False
 
 
if __name__ == '__main__':
 
    A = [2, 7, 4, 0, 9, 5, 1, 3]
    sum = 20
 
    if not quadTuple(A, len(A), sum):
        print("Quadruplet Doesn't Exist")
