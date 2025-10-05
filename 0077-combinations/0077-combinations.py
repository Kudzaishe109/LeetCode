class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        combs = []

        def dfs(i):
            if len(combs) == k  :
                res.append(combs[:])
                return 
            if i > n:
                return
            combs.append(i)
            
            dfs(i + 1)
            combs.pop()
            dfs(i + 1)
            
        dfs(1)
        return res

