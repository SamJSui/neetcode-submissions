class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        n = len(candidates)
        candidates.sort()

        def dfs(i, summ, path):
            print(f'i: {i}, summ: {summ}, path: {path}')
            if summ == 0: 
                ret.append(path)
                return
            if i >= n or summ < 0: 
                return 0
            
            dfs(i+1, summ-candidates[i], path+[candidates[i]])
            while i < n-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, summ, path)
            
        dfs(0, target, [])
        return ret