import heapq

priority = []

for value in [5, 2, 7, 1]:
    heapq.heappush(priority, value)

print(heapq.heappop(priority))
print(heapq.heappop(priority))
print(sorted(priority))