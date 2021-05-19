#dp +binary search
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        segments = []
        for i in range(n):
            segments.append([startTime[i],endTime[i],profit[i]])
        
        segments.sort(key=lambda x:x[1])
        
        dp = [0]*n
        for i in range(n):
            # if we don't take i
            if i>0:
                dp[i] = dp[i-1]
            
            # if we take i
            l = 0
            r = i
            while l+1<r:
                mid = l+(r-l)//2
                if segments[mid][1]<=segments[i][0]:
                    l = mid
                else:
                    r = mid
            if segments[l][1]<=segments[i][0]:
                dp[i] = max(dp[i],dp[l]+segments[i][2])
            
            dp[i] = max(dp[i],segments[i][2])
        
        return dp[-1]
#only dp

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        segments = []
        for i in range(n):
            segments.append([startTime[i],endTime[i],profit[i]])
        
        segments.sort(key=lambda x:x[1])
        
        dp = [0]*n
        for i in range(n):
            # if we don't take i
            if i>0:
                dp[i] = dp[i-1]
            
            # if we take i
            
            for j in range(i-1,-1,-1):
                if segments[j][1]<=segments[i][0]:
                    dp[i] = max(dp[i],dp[j]+segments[i][2])
                    break
            
            # take into count when interval i is the first one
            dp[i] = max(dp[i],segments[i][2])
        
        return dp[-1]
