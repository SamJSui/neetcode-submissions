class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        const int maxElement = *max_element(piles.begin(), piles.end());
        int l = 1, r = maxElement;
        while (l <= r) {
            int mid = l + (r-l) / 2;
            if (timeEating(mid, piles) <= h) {
                r = mid-1;
            }
            else l = mid+1;
        }
        return l;
    }

    int timeEating(int rate, vector<int>& piles) {
        int timeTaken = 0;
        for (int pile : piles) {
            timeTaken += (pile+rate-1)/rate;
        }
        return timeTaken;
    }
};
