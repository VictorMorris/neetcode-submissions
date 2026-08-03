class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = {i: [] for i in range(numCourses)}
        order = []
        visited = set()   # courses currently on the recursion stack (cycle check)
        finished = set()  # courses fully processed and added to order

        for crs, preReq in prerequisites:
            crsMap[crs].append(preReq)

        def dfs(crs):
            if crs in finished:
                return True
            if crs in visited:
                return False

            visited.add(crs)
            for preReq in crsMap[crs]:
                if not dfs(preReq):
                    return False
            visited.remove(crs)

            finished.add(crs)
            order.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order