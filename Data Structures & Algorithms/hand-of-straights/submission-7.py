class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        cnter = {}
        for card in hand:
            cnter[card] = cnter.get(card, 0)-1
        maxheap = []
        for card in cnter:
            heapq.heappush(maxheap, (cnter[card], card))
        print(f"cnter: {cnter}", "\n")

        while maxheap:
            print(f"maxheap: {maxheap}")
            print(f"cnter: {cnter}")
            cnt, top = heapq.heappop(maxheap)
            print(cnt, top)
            while cnt != cnter[top]:
                heapq.heappush(maxheap, (cnter[top], top))
                cnt, top = heapq.heappop(maxheap)

            if cnt >= 0: continue

            for card in range(top, top+groupSize):
                print(f"card: {card}")
                if card not in cnter or cnter[card] >= 0: 
                    print(cnter)
                    return False
                cnter[card] += 1
            if cnt+1 < 0: heapq.heappush(maxheap, (cnt+1, top))
            print("\n")
        return True