class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for ast in asteroids:
            if not result or ast > 0:
                result.append(ast)
                continue

            while True:
                if not result or result[-1] < 0:
                    result.append(ast)
                    break

                if result[-1] > -ast:
                    break
                elif result[-1] == -ast:
                    result.pop()
                    break
                else:
                    result.pop()

        return result

"""
5, 10, -5
5, 10 -> 5, 10
10, -5 -> 10
"""
