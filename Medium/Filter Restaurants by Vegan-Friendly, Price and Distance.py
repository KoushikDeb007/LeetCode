class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        res = []
        rlen = len(restaurants)
        for i in range(rlen):
            if (veganFriendly == 0 or restaurants[i][2] == veganFriendly) and restaurants[i][3] <= maxPrice and \
                    restaurants[i][4] <= maxDistance:
                res.append((restaurants[i], i + 1))
        res.sort(reverse=True, key=lambda x: (x[0][1], x[0][0]))

        ind = []
        for i in res:
            ind.append(i[0][0])
        return ind


