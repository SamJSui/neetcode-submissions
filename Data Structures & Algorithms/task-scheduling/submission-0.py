class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = {}
        for task in tasks:
            cnt[task] = cnt.get(task, 0)+1
        
        maxheap = []
        q = deque()
        for task in cnt:
            heapq.heappush(maxheap, (-cnt[task], task))
        
        time = 0
        while maxheap or q:
            print(time)
            print(maxheap)
            print(q, '\n')

            if q and q[0][0] == time:
                t, task = q.popleft()
                heapq.heappush(maxheap, task)
            if maxheap:
                cnt, task = heapq.heappop(maxheap)
                cnt += 1
                if cnt < 0:
                    q.append((time+n+1, (cnt, task)))
            time += 1
        return time
