class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        # print(a[:-1])
        ar, ac = map(int, a[:-1].split("+"))
        br, bc = map(int, b[:-1].split("+"))
        return f"{ar*br-ac*bc}+{ar*bc+ac*br}i"