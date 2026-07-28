class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-s for s in stones]
        heapq.heapify(stoneHeap)
        while len(stoneHeap) > 1:
            stone1 = heapq.heappop(stoneHeap)
            stone2 = heapq.heappop(stoneHeap)

            if stone1 == stone2:
                pass
            else:
                heapq.heappush(stoneHeap, stone1-stone2)
        
        return -stoneHeap[0] if stoneHeap else 0
        