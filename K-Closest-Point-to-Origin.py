class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        result=[]
        for x,y in points:
            distance=sqrt((x**2) + (y**2))
            minHeap.append([distance,x,y])
        heapq.heapify(minHeap)
        while k>0:
            dist,x,y=heapq.heappop(minHeap)
            result.append([x,y])
            k-=1
        return result
