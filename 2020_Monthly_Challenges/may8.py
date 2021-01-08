# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.
# Constraints: 
#   2 <= coordinates.length <= 1000
#   coordinates[i].length == 2
#   -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#   coordinates contains no duplicate point

class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        num_points = len(coordinates)
        # if we have two points, we have a line 
        if num_points == 2: 
            return True
        else: 
            base_vector = [coordinates[1][0]-coordinates[0][0],coordinates[1][1]-coordinates[0][1]]
            for i in range(2,num_points):
                x = coordinates[i][0]-coordinates[0][0]
                y = coordinates[i][1]-coordinates[0][1]
                if x*base_vector[1]-y*base_vector[0] != 0:
                    return False
            return True
        