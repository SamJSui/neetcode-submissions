class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int n = words.size();
        std::unordered_map<int, int> freq;
        for (const string& word : words) {
            for (const char& c : word) {
                freq[c]++;
            }
        }
        for (auto it : freq) {
            if (it.second % n != 0) return false;
        }
        return true;
    }
};