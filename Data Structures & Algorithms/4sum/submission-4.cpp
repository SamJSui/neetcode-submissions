class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> quads;

        int i = 0;
        while (i < n-3) {
            int j = i+1;
            while (j < n-2) {

                int l = j+1, r = n-1;
                long long sumIJ = nums[i]+nums[j];
                while (l < r) {
                    
                    long long sum = sumIJ+nums[l]+nums[r];
                    if (target-sum == 0) {
                        quads.push_back(vector<int>({nums[i], nums[j], nums[l], nums[r]}));
                        while (l < r && nums[l] == nums[l+1]) ++l;
                        ++l;
                        while (r > l && nums[r] == nums[r-1]) --r;
                        --r;
                    }
                    else if (sum < target) {
                        ++l;
                    }
                    else {
                        --r;
                    }
                }

                while (j < n-1 && nums[j] == nums[j+1]) ++j;
                ++j;
            }
            while (i < n-1 && nums[i] == nums[i+1]) ++i;
            ++i;
        }
        return quads;
    }
};