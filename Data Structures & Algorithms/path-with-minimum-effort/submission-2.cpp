class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        dist[0][0] = 0;
        
        priority_queue<vector<int>, vector<vector<int>>, greater<>> minheap;
        minheap.push({0, 0, 0});
        int dir[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};

        while (!minheap.empty()) {
            auto top = minheap.top();
            minheap.pop();

            int height = top[0];
            int i = top[1], j = top[2];
            if (i == m-1 && j == n-1) return height;
            if (dist[i][j] < height) continue;

            for (auto d : dir) {
                int ni = i+d[0];
                int nj = j+d[1];
                if (ni < 0 || ni >= m || nj < 0 || nj >= n) continue;

                int diff = abs(heights[i][j] - heights[ni][nj]);
                if (max(diff, height) < dist[ni][nj]) {
                    dist[ni][nj] = max(diff, height);
                    minheap.push({max(diff, height), ni, nj});
                }
            }
        }
        return 0;
    }
};