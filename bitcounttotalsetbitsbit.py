def getSetBitsFromOneToN(N):
    two = 2
    ans = 0
    n = N
    while(n != 0)
    {
        ans += int(N / two) * (two >> 1)
        if((N & (two - 1)) > (two >> 1) - 1):
            ans += (N&(two - 1)) - (two >> 1) + 1
        two <<= 1; 
        n >>= 1;
    }
    return ans
