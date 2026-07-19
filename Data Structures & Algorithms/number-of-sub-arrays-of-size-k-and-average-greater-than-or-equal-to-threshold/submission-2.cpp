class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int kThresh = k*threshold;
        int runningSum = accumulate(arr.begin(), arr.begin()+k, 0);
        int n = arr.size();
        int l = 0, r = k;
        int subarrays = 0;
        while (true) {
        //     printf("%d %d: %d >= %d\n", l, r, runningSum, kThresh);
            if (runningSum >= kThresh) subarrays++;
            if (r >= n) break;
            runningSum -= arr[l++];
            runningSum += arr[r++];
        }
        return subarrays;
    }
};