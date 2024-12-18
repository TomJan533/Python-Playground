from typing import List
import pytest


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for number in nums:
            if number not in hash_set:
                hash_set.add(number)
            else:
                return True

        return False
    
@pytest.mark.unit
@pytest.mark.parametrize(
    "input_data, expected_result",  # Parametrized inputs and expected outputs
    [
        ([1, 2, 3, 1], True),   # Case where there's a duplicate
        ([1, 2, 3], False),     # Case where there are no duplicates
        ([1], False),           # Case with a single element
        ([], False),           # Case with no elements
    ]
)
def test_hasDuplicate(input_data, expected_result):
    solution = Solution()
    assert solution.hasDuplicate(input_data) == expected_result