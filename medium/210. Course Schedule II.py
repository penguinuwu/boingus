"""
11:18.56
O(v+e)
sO(v+e)
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(lambda: {"prereqs": set(), "dependents": set()})
        for c, p in prerequisites:
            courses[c]["prereqs"].add(p)
            courses[p]["dependents"].add(c)

        # take all the courses without prereqs
        semester = [c for c in range(numCourses) if len(courses[c]["prereqs"]) == 0]
        results = []
        courses_taken = 0

        while semester:
            results.extend(semester)
            next_semester = []

            for course in semester:
                courses_taken += 1

                # remove blocker for dependent courses
                for dependent in courses[course]["dependents"]:
                    courses[dependent]["prereqs"].remove(course)

                    # take course next semester if no prereqs remain
                    if len(courses[dependent]["prereqs"]) == 0:
                        next_semester.append(dependent)

            semester = next_semester
            print(semester)

        return results if courses_taken == numCourses else []
