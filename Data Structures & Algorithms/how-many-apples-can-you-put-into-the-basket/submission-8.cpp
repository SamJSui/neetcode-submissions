class Solution {
public:
    int maxNumberOfApples(vector<int>& weight) {
        int freq[1001] = {0};
        for (int& w : weight) {
            freq[w]++;
        }
        int apples = 0;
        int remaining = 5000;
        for (int i = 1; i <= 1000; ++i) {
            int able = remaining / i;
            int actual = min(freq[i], able);
            apples += actual;
            remaining -= actual * i;
            if (remaining < 0) break;
            // printf("%d %d: %d %d %d %d\n", i, freq[i], able, actual, apples, remaining);
        }
        return apples;
    }
};