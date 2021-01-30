class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # count = Counter(nums)
        # arr = list(count.keys())
        def partition(arr, low, high):
            i = low
            pivot = arr[high]
            for j in range(low, high):
                if arr[j] < pivot:
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
        quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
        # print(arr)
        return nums[len(nums) - k]

        # nums.sort(reverse=True)
        # return nums[k-1]
