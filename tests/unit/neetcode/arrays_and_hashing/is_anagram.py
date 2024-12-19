import pytest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = {}
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        
        for char in t:
            if char not in s_count or s_count[char] == 0:
                return False
            s_count[char] -= 1
        
        return True


@pytest.mark.unit
@pytest.mark.parametrize(
    "s, t, expected_result",
    [
        ("anagram", "nagaram", True),   # Case where the strings are anagrams
        ("rat", "car", False),          # Case where the strings are not anagrams
    ]
)
def test_isAnagram(s, t, expected_result):
    solution = Solution()
    assert solution.isAnagram(s, t) == expected_result
