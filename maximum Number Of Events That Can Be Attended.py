from collections import defaultdict
from heapq import heappush ,heappop
from math import inf
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        start_day,end_day=inf,0
        events_dict = defaultdict(list)
        
        for start,end in events:
            events_dict[start].append(end)
            start_day=min(start_day,start)
            end_day=max(end_day,end)

        min_heap=[]
        attended=0
        for day in range(start_day,end_day+1):

            while min_heap and min_heap[0]< day:
                heappop(min_heap)

            for end in events_dict[day]:
                heappush(min_heap,end)
            
            if min_heap:
                attended+=1
                heappop(min_heap)


        return attended
           
        
