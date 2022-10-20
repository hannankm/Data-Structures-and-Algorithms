class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda t:t[1])
        heap=[]
        currPass=0
        for i in trips:
            passengers, start, end=i
            while heap and heap[0][0]<=start:
                currPass-=heap[0][1]
                heapq.heappop(heap)
            currPass+=passengers
            if currPass>capacity:
                return False
            heapq.heappush(heap,[end, passengers])
        return True
