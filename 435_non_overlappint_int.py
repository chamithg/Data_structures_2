class Solution:
    def eraseOverlapIntervals(self, intervals):
     
        intervals.sort(key=lambda x: x[1]) 
        #  this will sort the intervals according to the end point
        max_end, output = float('-inf'), 0
        for start,end in intervals:
            if start>= max_end:
                max_end = end
            else:
                output +=1
        return output



intervals = [[1,2],[2,3],[3,4],[1,3]]

obj = Solution()
print(obj.eraseOverlapIntervals(intervals))