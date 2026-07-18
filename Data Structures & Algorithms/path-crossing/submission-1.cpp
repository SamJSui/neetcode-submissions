class Solution {
public:
    bool isPathCrossing(string path) {
        set<pair<int, int>> visited;
        visited.insert({0, 0});
        int x = 0, y = 0;
        for (char c : path) {
            switch (c) {
                case 'N':
                    y++;
                    break;
                case 'S':
                    y--;
                    break;
                case 'W':
                    x--;
                    break;
                case 'E':
                    x++;
                    break;
            }
            if (visited.find({x, y}) != visited.end()) return true;
            // printf("%c %d %d\n", c, x, y);
            visited.insert({x, y});
        }
        return false;
    }
};