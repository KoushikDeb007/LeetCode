class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        # array_of_sets = [set(company) for company in favoriteCompanies]
        # print(array_of_sets)
        # result = []
        # for i in range(len(favoriteCompanies)):
        #     add = True
        #     for j in range(len(favoriteCompanies)):
        #         if i != j:
        #             if i==1 and j==4:
        #                 print(array_of_sets[i] < array_of_sets[j])
        #             if array_of_sets[i] < array_of_sets[j]:
        #                 add = False
        #                 break
        #     if add:
        #         result.append(i)
        # return result
        #         i = 0
        #         ans = []

        #         while i < len(favoriteCompanies):
        #             if all(not set(favoriteCompanies[i]).issubset(favoriteCompanies[j]) for j in range(len(favoriteCompanies)) if i!=j):
        # 				ans.append(i)
        #             i += 1

        #         return ans
        favcomp_sets = [set(favcomp) for favcomp in favoriteCompanies]

        unique_users = []
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i == j or len(favcomp_sets[i]) >= len(favcomp_sets[j]):
                    continue
                if favcomp_sets[i].issubset(favcomp_sets[j]):
                    break
            else:
                unique_users.append(i)
        return unique_users
