class Solution:
    def queensAttacktheKing(self, queens, king) :

        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        x, y = king[0], king[1]
        dx = [-1, 0, 1, 0, -1, -1, 1, 1]
        dy = [0, 1, 0, -1, -1, 1, 1, -1]
        count = []
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            while (0 <= xx <= 7 and 0 <= yy <= 7):
                # print([xx,yy] in queens)
                if [xx, yy] in queens:
                    count.append([xx, yy])
                    break
                xx += dx[i]
                yy += dy[i]

        return count