class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.cache = matrix

        for row in range(len(self.cache)):
            for col in range(len(self.cache[row])):
                if col > 0:
                    self.cache[row][col] += self.cache[row][col - 1]
            for col in range(len(self.cache[row])):
                if row > 0:
                    self.cache[row][col] += self.cache[row - 1][col]

    def __get_cache(self, row: int, col: int):
        if row < 0 or col < 0 or row >= len(self.cache) or col >= len(self.cache[row]):
            return 0
        return self.cache[row][col]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        everything = self.__get_cache(row2, col2)
        top = self.__get_cache(row2, col1 - 1)
        left = self.__get_cache(row1 - 1, col2)

        # top left corner got subtracted twice, so we add it back
        top_left_corner = self.__get_cache(row1 - 1, col1 - 1)

        return everything - top - left + top_left_corner


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
