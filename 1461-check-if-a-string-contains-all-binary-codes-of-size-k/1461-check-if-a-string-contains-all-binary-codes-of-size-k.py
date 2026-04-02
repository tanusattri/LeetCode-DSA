class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total_needed=1 << k
        found_codes= set()
        for i in range(len(s) - k + 1):
            substring= s[i : i + k]
            found_codes.add(substring)
            if len(found_codes)==total_needed:
                return True
        return len(found_codes)==total_needed