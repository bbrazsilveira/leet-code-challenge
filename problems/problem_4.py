import math
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    merged = sorted(nums1 + nums2)
    merged_length = len(merged)

    half = merged_length // 2
    if merged_length % 2 == 1:
        return merged[math.floor(half)]
    else:
        return (merged[half - 1] + merged[half]) / 2


result = find_median_sorted_arrays([1, 2], [3, 4])
print(result)
