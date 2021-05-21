class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            L = len(s)
            dp = [False]*(L+1)
            dp[0]=True
            for i in range(1,L+1):
                for j in range(i):
                    if dp[j] and s[j:i] in wordDict:
                        print(s[j:i])
                        dp[i] = True
            return dp[-1]
