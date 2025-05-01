"""
30:33.35
O(v+e)
sO(v+e)
check solution after 3mins
simplify data structures, sets are not required
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # record number of incoming edges
        prereq_count = [0] * numCourses

        # make adjacency list of courses that depend on this
        required_by = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            required_by[prereq].append(course)
            prereq_count[course] += 1

        # trim roots
        available_courses = deque([c for c in range(numCourses) if prereq_count[c] == 0])
        taken_courses = 0
        while available_courses:
            # take course
            prereq = available_courses.popleft()
            taken_courses += 1

            # check all courses dependent on this course
            for dependent in required_by[prereq]:
                prereq_count[dependent] -= 1

                # check if course now has no dependencies
                if prereq_count[dependent] == 0:
                    available_courses.append(dependent)

        return taken_courses == numCourses
