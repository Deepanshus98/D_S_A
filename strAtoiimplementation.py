# Python program for implementation of atoi

# A simple atoi() function


def myAtoi(string):
    res = 0

    # Iterate through all characters of
    #  input string and update result
    for i in xrange(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))

    return res


# Driver program
string = "89789"

# Function call
print myAtoi(string)



def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack=='' and needle!='':return -1
        if needle=='':return 0
        
        for i in range (len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                j=0
                while j<len(needle):
                    if haystack[i+j]!=needle[j]:break
                    else:j+=1
                if j==len(needle):return i
        return -1
