class Solution:
	def countArrangement(self, N: int) -> int:
		ans = 0
		checked = [False for _ in range(N+1)]

		def backtrack(candidate):
			if len(candidate) == N:
				nonlocal ans
				ans += 1
				return

			for num in range(1, N+1):
				i = len(candidate) + 1
				if checked[num] == False and (num % i == 0 or i % num == 0):
					candidate.append(num)
					checked[num] = True
					backtrack(candidate)
					candidate.pop()
					checked[num] = False

		backtrack([])
		return ans