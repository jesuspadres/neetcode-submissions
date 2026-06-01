class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class Node:
            def __init__(self, val):
                self.prereqs = []
                self.val = val

                
        courses = [Node(i) for i in range(numCourses)]

        for p in prerequisites:
            a = p[0]
            b = p[1]

            courses[a].prereqs.append(courses[b])

        retList = []
        retSet = set()

        def dfs(course, visited):
            if course in visited:
                return False

            visited.add(course)
            for p in course.prereqs:
                if not dfs(p, visited):
                    return False
            visited.remove(course)
            if course.val not in retSet:
                retList.append(course.val)
                retSet.add(course.val)

            return True

        for course in courses:
            if not dfs(course, set()):
                return []

        return retList