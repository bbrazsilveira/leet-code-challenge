from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    total_nums = len(nums)

    for i in range(total_nums):
        if i >= total_nums - 1:
            break

        for j in range(i + 1, total_nums):
            sum_ = nums[i] + nums[j]

            if sum_ == target:
                return [i, j]

    return []
