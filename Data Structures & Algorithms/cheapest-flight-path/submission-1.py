class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for flight in flights:
            s, d, w = flight
            adj[s].append((d, w))
        
        print(f'adj {adj}')

        ret = float('inf')
        minheap = [(0, src, -1)]
        while minheap:
            price, top, stops = heapq.heappop(minheap)
            print(price, top, stops)
            if top == dst:
                ret = min(ret, price)

            for nei in adj[top]:
                dest, weight = nei
                if dest + price > ret or stops+1 > k: 
                    print('SKIPPED')
                    continue
                heapq.heappush(minheap, (weight+price, dest, stops+1))
            
        return -1 if ret == float('inf') else ret