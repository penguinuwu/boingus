"""
15:22.94
O(n^2) but time<=100 and len(clips)<=100 so its O(1) lmao
sO(n)
"""

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # store longest clip of each starting point
        clips_start_to_end = defaultdict(lambda: 0)
        for start, end in clips:
            if start > time:
                continue # skip clips we dont need
            clips_start_to_end[start] = max(clips_start_to_end[start], end)

        # run bfs starting from first clip
        curr_clip_start = 0
        curr_clip_end = clips_start_to_end[curr_clip_start]
        clips_count = 1

        # stop loop and return when clip reaches goal timestamp
        while curr_clip_end < time:
            max_clip_start, max_clip_end = 0, 0

            # look for the next clip with the latest end timestamp
            # within the current clip [start, finish]
            for start in range(curr_clip_start+1, curr_clip_end+1):
                if clips_start_to_end[start] > max_clip_end:
                    max_clip_start = start
                    max_clip_end = clips_start_to_end[start]

            if max_clip_end == 0:
                return -1
            else:
                curr_clip_start = max_clip_start
                curr_clip_end = max_clip_end
                clips_count += 1

        return clips_count
