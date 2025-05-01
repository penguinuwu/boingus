"""
24:22.59
O(v+e)
sO(v+e)
check solution after 3mins
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make adjacency list
        adj_lst = defaultdict(lambda: {"required": set(), "required_by": set()})
        for course, prereq in prerequisites:
            adj_lst[course]["required"].add(prereq)
            adj_lst[prereq]["required_by"].add(course)

        # trim roots
        roots = [c for c in range(numCourses) if len(adj_lst[c]["required"]) == 0]
        taken_courses = 0

        while roots:
            new_roots = []

            # take course
            for course in roots:
                taken_courses += 1

                # check all courses dependent on this course
                for required_by in adj_lst[course]["required_by"]:
                    adj_lst[required_by]["required"].remove(course)

                    # check if course now has no dependencies
                    if len(adj_lst[required_by]["required"]) == 0:
                        new_roots.append(required_by)

            roots = new_roots

        return taken_courses == numCourses
