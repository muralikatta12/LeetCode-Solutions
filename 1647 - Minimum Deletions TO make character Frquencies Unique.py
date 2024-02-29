from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:

        count=Counter(s)
       
        seen=set()
        min_char=0
        for value in count.values():
            freq=value
            while freq > 0 and freq in seen:
                freq-=1
                min_char+=1
            
            seen.add(freq)
        return min_char
        
