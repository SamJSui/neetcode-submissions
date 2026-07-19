class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int kThresh = k*threshold;
        int runningSum = accumulate(arr.begin(), arr.begin()+k, 0);
        int n = arr.size();
        int subarrays = 0;
        if (runningSum >= kThresh) subarrays++;

        for (int r = k; r < n; r++) {
            runningSum += arr[r];
            runningSum -= arr[r-k];
            if (runningSum >= kThresh) subarrays++;
        }
        return subarrays;
    }
};