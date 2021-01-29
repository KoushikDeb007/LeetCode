"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


import collections


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        idtoIndex = {}
        for i in range(len(employees)):
            idtoIndex[employees[i].id] = i

        queue = collections.deque(employees[idtoIndex[id]].subordinates)
        res += employees[idtoIndex[id]].importance

        while queue:
            res += employees[idtoIndex[queue[0]]].importance
            queue.extend(employees[idtoIndex[queue[0]]].subordinates)
            queue.popleft()
        return res