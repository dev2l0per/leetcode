from typing import List

def partition(arr: List[int], start: int, end: int, pivotIndex: int) -> int:
    pivot = arr[pivotIndex]
    arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end]

    curr = start

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[curr] = arr[curr], arr[i]
            curr += 1
    arr[end], arr[curr] = arr[curr], arr[end]
    return curr

def quickSelect(arr: List[int], start: int, end: int, k: int):
    if start == end:
        return arr[start]
    pivot = end
    pivot = partition(arr, start, end, pivot)

    if pivot == k:
        return arr[pivot]
    elif pivot < k:
        return quickSelect(arr, pivot + 1, end, k)
    else:
        return quickSelect(arr, start, pivot - 1, k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)