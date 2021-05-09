# Function to check if `X` and `Y` are anagrams or not
def isAnagram(X, Y):
 
    # if X's length is not the same as Y's, they can't be an anagram
    if len(X) != len(Y):
        return False
 
    # create an empty dictionary
    freqX = {}
 
    # maintain the count of each character of `X` on the dictionary
    for i in range(len(X)):
        freqX[X[i]] = freqX.get(X[i], 0) + 1
 
    # create a second dictionary
    freqY = {}
 
    # maintain a count of each character of `Y` on the dictionary
    for i in range(len(Y)):
        freqY[Y[i]] = freqY.get(Y[i], 0) + 1
 
    # return true if both dictionaries have the same content
    return freqX == freqY
 
 
if __name__ == '__main__':
 
    X = "tommarvoloriddle"        # Tom Marvolo Riddle
    Y = "iamlordvoldemort"        # I am Lord Voldemort
 
    if isAnagram(X, Y):
        print("Anagram")
    else:
        print("Not an Anagram")
