class Solution:
    def countSubstrings(self, s: str) -> int:
        cache = {}
        n = len(s)
        count = 0

        for start in range(n):
            count += 1

            for length in range(2, n - start + 1):
                ss = s[start:start+length]
                if ss in cache:
                    count += cache[ss]
                    continue

                for offset in range(length // 2):
                    s1 = s[start + offset]
                    s2 = s[start + (length - 1) - offset]
                    if s1 != s2:
                        cache[ss] = 0
                        break
                else:
                    count += 1
                    cache[ss] = 1

        return count
