"""
1:38.33
O(nlogn + klogk) (sort len(n) then sort len(k))
sO(k) (slice return array)
preread solution
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda a: abs(a - x))
        return sorted(arr[:k])
