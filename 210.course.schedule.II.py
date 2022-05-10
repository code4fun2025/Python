class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        """
        [1,0],[2,0],[3,1],[3,2]
    
        0  []    
        1  [0]
        2  [0]
        3  [1, 2]

        return: [0, 1, 2, 3] or [0, 2, 1, 3], if there's loop, return []
        """
        
        preMap = {i:[] for i in range(numCourses)}
        # map to prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # start visisted table with 0 (unknown), 1: visisting, 2: visited
        visited = {i:0 for i in range(numCourses)}
        
        # return array starts with empty array
        orderedCourse = []
        
        def dfs(crs):
            # detects loop, return empty array
            if visited[crs] == 1:
                return []
            # found possible schedule, return courses 
            if visited[crs] == 2:
                return orderedCourse
        
            # mark visiting and perform DFS for the prerequisites 
            visited[crs] = 1
            for pre in preMap[crs]:
                if dfs(pre) == []: 
                    return []
                
            # no loop detected, add course to return array 
            visited[crs] = 2
            orderedCourse.append(crs)
            
            return orderedCourse
        
        for i in range(numCourses):
            if dfs(i) == []:
                return []
        
        return orderedCourse
