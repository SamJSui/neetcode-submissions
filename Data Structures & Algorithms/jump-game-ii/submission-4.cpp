class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> memo(n, -1);
        return dfs(0, nums, memo);
    }
    int dfs(int i, vector<int>& nums, vector<int>& memo) {
        if (i >= nums.size()-1) return 0;
        if (memo[i] != -1) {
            return memo[i];
        }
        if (nums[i] == 0) return 1e9;
        
        int res = 1e9;
        for (int j = min((int)nums.size() - 1, i + nums[i]); j > i; --j) {
            res = min(res, dfs(j, nums, memo) + 1);
        }
        return memo[i] = res;
    }
};