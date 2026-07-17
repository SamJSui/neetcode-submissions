class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        def finished(piles, mid, h):
            time = 0
            for pile in piles:
                if mid > pile: 
                    time += 1
                    continue
                time += pile // mid
                if pile % mid != 0: time += 1
            print(f'time: {time} h: {h}')
            return h >= time
        
        while l <= r:
            mid = (l+r)//2
            print(f'l: {l}, r: {r}, mid: {mid}')
            if finished(piles, mid, h):
                r = mid-1
            else:
                l = mid+1
        return l