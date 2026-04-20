class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        d = lambda x, y: x**2 + y**2
        for x, y in points:
            dist_origin = -d(x, y)
            if len(heap) == k:
                heapq.heappushpop(heap, [dist_origin, x, y])
            else:
                heapq.heappush(heap, [dist_origin, x, y])

        return list(map(lambda x: x[1:], heap))