#Code
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_gas,current_gas=0,0
        s_index=0
        for i in range(len(gas)):

            current_gas+=gas[i]-cost[i]

            total_gas+=gas[i]-cost[i]
            if current_gas<0:

                current_gas=0
                #if current index is negative starting from next station
                
                s_index=i+1
        return s_index if total_gas>=0 else -1
