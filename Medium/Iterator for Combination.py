# class CombinationIterator:

#     def __init__(self, characters: str, combinationLength: int):
#         self.res = []
#         self.combination(0,characters,combinationLength,'',self.res)
#         self.n = 0
#         # print(self.res)


#     def next(self) -> str:
#         self.n+=1
#         return self.res[self.n-1]

#     def hasNext(self) -> bool:
#         if self.n<len(self.res):
#             return True
#         return False

#     def combination(self,ind,char,clen,path,res):
#         if len(path)==clen:
#             res.append(path)
#             return
#         for i in range(ind,len(char),1):
#             self.combination(i+1,char,clen,path+char[i],res)


# # Your CombinationIterator object will be instantiated and called as such:
# # obj = CombinationIterator(characters, combinationLength)
# # param_1 = obj.next()
# # param_2 = obj.hasNext()
from os.path import commonprefix


class CombinationIterator:

    def __init__(self, characters, combinationLength):
        self.c = characters
        self.len = combinationLength
        self.state = ""

    def next(self):
        if self.state == "":
            self.state = self.c[:self.len]
        else:
            end = len(commonprefix([self.c[::-1], self.state[::-1]]))
            place = self.c.index(self.state[-end - 1])
            self.state = self.state[:-end - 1] + self.c[place + 1: place + 2 + end]
        return self.state

    def hasNext(self):
        return self.state != self.c[-self.len:]