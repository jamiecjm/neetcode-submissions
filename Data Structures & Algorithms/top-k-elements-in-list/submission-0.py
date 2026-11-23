class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []

        for n in nums:
            count[n] += 1

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if (len(heap)) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result