# Function to segment given string into a space-separated
# sequence of one or more dictionary words
def wordBreak(dict, str, out=""):
 
    # if the end of the string is reached,
    # print the output string
    if not str:
        print(out)
        return
 
    for i in range(1, len(str) + 1):
        # consider all prefixes of the current string
        prefix = str[:i]
 
        # if the prefix is present in the dictionary, add it to the
        # output string and recur for the remaining string
        if prefix in dict:
            wordBreak(dict, str[i:], out + " " + prefix)
 
 
# Word Break Problem Implementation in Python
if __name__ == '__main__':
 
    # List of strings to represent a dictionary
    dict = [
        "self", "th", "is", "famous", "Word",
        "break", "b", "r", "e", "a", "k", "br",
        "bre", "brea", "ak", "problem"
    ]
 
    # input string
    str = "Wordbreakproblem"
 
    wordBreak(dict, str)
