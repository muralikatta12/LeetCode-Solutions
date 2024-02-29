class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time=0
        colors=list(colors)
        n=len(colors)
        i=0
        while i<n-1:
            if colors[i]==colors[i+1]:
                min_index= i if neededTime[i]<neededTime[i+1] else i+1
                min_time=neededTime[min_index]
                time+=min_time
                colors.pop(min_index)
                neededTime.pop(min_index)
                n-=1
            else:
                i+=1
        return time
    
