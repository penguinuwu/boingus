class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev_arrive = -1
        count = 0
        for p, s in sorted(zip(position, speed), reverse=True):
            curr_arrive = (target - p) / s
            # slower cars will become the new bottleneck
            if curr_arrive > prev_arrive:
                prev_arrive = curr_arrive
                count += 1
        return count

"""
Input: target = 12, position = , speed = 

[2,4,1,1,3]
[10,8,0,5,3]

 0  1  2  3  4  5  6  7  8  9 10 11 12
__ __ __ __ __ __ __ __ __ __ __ __ __
                               0     1
                         0           1
 0  1  2  3  4  5  6  7  8  9 10 11 12
                0  1  2  3  4  5  6  7
          0        1  2  3  4  5  6  7

                0  1  2  3  4  5  6  7
          0        1        2        3

10, 12
8, 12
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
5, 6, 7, 8, 9, 10, 11, 12
3, 6, 9, 12


10, 8,0,5,3


[8,3,7,4,6,5]
 0  1  2  3  4  5  6  7  8  9 10
__ __ __ __ __ __ __ __ __ __ __
                         0     1
                      0        1
                   0           1
                0           1  2
             0           1     2
          0           1        2
# i guess this doesnt count as getting to the target together...


"""
