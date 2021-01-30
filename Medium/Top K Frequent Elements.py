class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = list(count.keys())

        def partition(arr, low, high):
            i = low
            pivot = arr[high]
            for j in range(low, high):
                if count[arr[j]] < count[pivot]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[i], arr[high] = arr[high], arr[i]
            return i

        def quickSelect(arr, low, high, k):
            if low < high:
                pivot = partition(arr, low, high)
                # print(arr,pivot)
                if pivot == k:
                    return
                elif pivot < k:
                    quickSelect(arr, pivot + 1, high, k)
                else:
                    quickSelect(arr, low, pivot - 1, k)

        # print(arr,count)
        quickSelect(arr, 0, len(arr) - 1, len(arr) - k)
        # print(arr)
        return arr[len(arr) - k:]

        # if k == len(nums):
        #     return nums
        # count = Counter(nums)
        # res = []
        # for key,v in count.most_common():
        #     if k==0:
        #         break
        #     res.append(key)
        #     k-=1
        # return res
        # print(count)
        # print(count.keys())
        # print(count.values())
        # return heapq.nlargest(k, count.keys(), key = count.get)

