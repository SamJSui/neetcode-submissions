class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(opened, closed, parenth):
            if closed == n:
                ret.append(parenth)
            if opened < n:
                dfs(opened+1, closed, parenth+'(')
            if closed < opened:
                dfs(opened, closed+1, parenth+')')
        dfs(0, 0, '')
        return ret