class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> freq;
        int pairs = 0;
        for (int num : nums) {
            if (freq.find(num) == freq.end()) {
                freq[num] = 1;
            }
            else {
                pairs += freq[num];
                freq[num]++;
            }
            // printf("%d %d %d\n", num, freq[num], pairs);
        }
        return pairs;
    }
};