class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int n = words.size();
        std::unordered_map<char, int> freq;
        for (const string& word : words) {
            for (const char& c : word) {
                freq[c]++;
            }
        }
        for (const auto& it : freq) {
            if (it.second % n != 0) return false;
        }
        return true;
    }
};