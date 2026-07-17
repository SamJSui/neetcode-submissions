class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(test_s):
            print('testing palindrome', test_s)
            return test_s == test_s[::-1]

        n = len(s)
        ret = []
        curr = []
        def dfs(i):
            print('current:', i)
            if i >= n:
                ret.append(curr.copy())
                return

            for j in range(i, n):
                tmp = s[i:j+1]
                if is_pal(tmp):
                    curr.append(tmp)
                    dfs(j+1)
                    curr.pop()
        dfs(0)
        return ret