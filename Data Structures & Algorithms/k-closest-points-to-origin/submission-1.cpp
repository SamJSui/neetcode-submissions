float calcManhattanDist(const vector<int>& v1) {
    return sqrt(v1[0]*v1[0]+v1[1]*v1[1]);
}

class CompareX {
public:
    bool operator() (const vector<int>& v1, const vector<int>& v2) {
        float dist1 = calcManhattanDist(v1);
        float dist2 = calcManhattanDist(v2);
        return dist1 > dist2;
    }
};

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        std::priority_queue<vector<int>, vector<vector<int>>, CompareX> closest;
        for (const vector<int>& point : points) {
            closest.push(point);
        }
        
        vector<vector<int>> ret;
        ret.reserve(k);
        while (k) {
            ret.push_back(closest.top());
            closest.pop();
            k--;
        }
        return ret;
    }
};