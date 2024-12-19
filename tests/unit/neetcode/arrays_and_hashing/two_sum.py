from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                
@pytest.mark.unit
@pytest.mark.parametrize(
    "nums, target, expected_result",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
)
def test_isAnagram(nums, target, expected_result):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected_result