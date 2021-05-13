class Solution:
    def countBits(self, num: int) -> List[int]:
        solution=[0]
        for i in range (1,num+1):
            if(i%2==0):
                solution.append(solution[i//2])
            else:
                solution.append(solution[i-1]+1)
        return solution
