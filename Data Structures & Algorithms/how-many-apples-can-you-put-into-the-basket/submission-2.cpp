class Solution {
public:
    int maxNumberOfApples(vector<int>& weight) {
        std::map<int, int> freq;
        for (int& w : weight) {
            freq[w]++;
        }
        int maxi = 5000;
        int apples = 0;
        for (auto& it : freq) {
            int able = maxi / it.first;
            int actual = min(it.second, able);
            maxi -= actual * it.first;
            apples += actual;
            // printf("%d %d: %d %d %d %d\n", it->first, it->second, able, actual, maxi, apples);
            if (maxi <= 0) break;
        }
        return apples;
    }
};
