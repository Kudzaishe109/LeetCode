class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        def dfs():
            #base case
            if len(perm) == len(nums):
                res.append(perm[::])
                return
            for num in nums:
                if num in perm:
                    continue
                perm.append(num)     
                dfs()
                #pop/backtrack
                perm.pop()
                #recurse
        dfs()
        return res
            
