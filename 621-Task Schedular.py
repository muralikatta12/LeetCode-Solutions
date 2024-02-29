#code 
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the number of times each task is repeated
        count_tasks = Counter(tasks)
        # finds tthe max_count
        max_count_tasks = max(count_tasks.values())
        # finds how many times max_freq is repeated
        max_freq = sum(freq == max_count_tasks for freq in count_tasks.values())
        # Calculate the number of idle states needed, which is defined by the formula:
        # (maximum frequency of any task - 1) * (n + 1) which gives the spaces between repetitions of the same task
        idle_time = (max_count_tasks - 1) * (n + 1)
        least_units = idle_time + max_freq
        return max(len(tasks), least_units)
