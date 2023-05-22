import heapq

n = int(input())
li = []

for i in range(n):
    heapq.heappush(li, int(input()))

result = 0

if len(li)==1:
    print(result)
else:
    for i in range(n-1):
        a = heapq.heappop(li)
        b = heapq.heappop(li)

        result += (a+b)
        heapq.heappush(li, a+b)
    print(result)