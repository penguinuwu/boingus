class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for start in range(n):
            count += 1

            offset = 1
            while start-offset >= 0 and start+offset-1 < n and s[start-offset] == s[start+offset-1]:
                count += 1
                offset += 1

            offset = 1
            while start-offset >= 0 and start+offset < n and s[start-offset] == s[start+offset]:
                count += 1
                offset += 1

        return count
