class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N is 1: 
            return 1
        
        if (N-1) > len(trust): 
            return -1

        trust_count = [0] * (N+1)
       
        for i, j in trust: 
           trust_count[i] -= 1
           trust_count[j] += 1
        
        for j in range(1, N+1):
            if trust_count[j] == N-1:
                return j

        return -1 