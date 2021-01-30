class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) <= 1 or K >= len(points):
            return points

        def dist(p):
            x, y = p
            return x * x + y * y

        def quickselect(n, k):
            if k == 1:
                return [min(n, key=dist)]

            if k == len(n):
                return n

            pivot = choice(n)
            # print(pivot)
            left = [i for i in n if dist(i) < dist(pivot)]
            mid = [i for i in n if dist(i) == dist(pivot)]
            right = [i for i in n if dist(i) > dist(pivot)]

            if len(left) > k:
                return quickselect(left, k)

            if len(left) <= k <= len(left) + len(mid):
                return left + mid[:k - len(left)]

            if len(left) + len(mid) < k:
                return left + mid + quickselect(right, k - len(left) - len(mid))

        return quickselect(points, K)
        # return heapq.nsmallest(K, points, key = lambda  x: x[0] * x[0] + x[1] * x[1])
#         newP = []
#         for i in points:
#             tup = (-math.sqrt(math.pow(i[0],2)+math.pow(i[1],2)),i)
#             if len(newP)<K:
#                 heapq.heappush(newP,tup)
#             else:
#                 if tup[0]>newP[0][0]:
#                     heapq.heapreplace(newP,tup)

#         return [val for key,val in newP]
# points.sort(key = lambda x: x[0]*x[0] + x[1]*x[1])
# return points[:K]
# newP = []
# for i in points:
#     newP.append((math.sqrt(math.pow(i[0],2)+math.pow(i[1],2)),i))
# heapq.heapify(newP)
# k = 1
# res = []
# while(k<=K):
#     k+=1
#     res.append(heappop(newP)[1])
# return res
# newP = []
# for i in points:
#     newP.append((-math.sqrt(math.pow(i[0],2) + math.pow(i[1],2)),i))
# heapify(newP)
# while(len(newP)>K):
#     heappop(newP)
# res = []
# while(newP):
#     res.append(heappop(newP)[1])
# return res

# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

#         def dist(p):
#             x=p[0]
#             y=p[1]
#             return x*x +y*y


#         points = sorted(points, key = lambda p: dist(p))
#         return points[:K]
