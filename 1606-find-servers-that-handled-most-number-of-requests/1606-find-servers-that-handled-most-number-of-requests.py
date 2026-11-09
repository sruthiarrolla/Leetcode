
from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i, (a, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= a:
                _, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            server = available.bisect_left(i % k)

            if server == len(available):
                server = 0

            assigned = available.pop(server)
            count[assigned] += 1

            heapq.heappush(busy, (a + l, assigned))

        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]
        