# https://leetcode.com/problems/employee-importance/

from collections import defaultdict

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total_impo = 0
        sub_graph = defaultdict(list)
        impo_graph = defaultdict(int)
        for employee in employees:
            impo_graph[employee.id] = employee.importance
            for subordinate in employee.subordinates:
                sub_graph[employee.id].append(subordinate)
        queue = [id]
        while queue:
            curr_id = queue.pop(0)
            total_impo += impo_graph[curr_id]
            for sub in sub_graph[curr_id]:
                queue.append(sub)
        return total_impo
    