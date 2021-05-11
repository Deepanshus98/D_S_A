class Solution:
  # @param s, a string
  # @param dict, a set of string
  # @return a boolean
  def wordBreak(self, s, dict):
    sLen = len(s)
    possible = [False for i in range(sLen + 1)]
    possible[0] = True

    for i in range(sLen):
      for j in range(i + 1):
        if possible[j] and s[j:i + 1] in dict:
            possible[i + 1] = True
            break;

    return possible[sLen]
