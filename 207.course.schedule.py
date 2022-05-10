class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visited state: 0 = unknown, 1 = visiting, 2 = visited/clear
        visited = {i:0 for i in range(numCourses)}
        
        def dfs(crs):
                # found loop/circle, return true            
                if visited[crs] == 1:
                    return False
                # found visited/clear state, return true
                if visited[crs] == 2:
                    return True
                
                # mark we are visiting the course
                visited[crs] = 1
                for pre in preMap[crs]:
                    # return if there's any prereq returns false
                    if not dfs(pre): 
                        return False
                    
                # no loop, mark the course to be visisted/cleared
                visited[crs] = 2
                return True
            
        # check every course, in case for isolated course 1->2, 3->5    
        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True
