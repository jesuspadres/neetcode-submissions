class Solution:
    

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        class Node:
            def __init__(self):
                self.prereqs = []

                
        courses = [Node() for _ in range(numCourses)]

        for p in prerequisites:
            a = p[0]
            b = p[1]

            courses[a].prereqs.append(courses[b])

        def dfs(course, visited):
            if course in visited:
                return False

            visited.add(course)
            for p in course.prereqs:
                if not dfs(p, visited):
                    return False
            visited.remove(course)

            return True

        for course in courses:
            if not dfs(course, set()):
                return False

        return True
            