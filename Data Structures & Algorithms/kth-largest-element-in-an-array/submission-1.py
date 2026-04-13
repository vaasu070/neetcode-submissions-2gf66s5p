class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify , heappop , heappush
        heapify(nums)
        while len(nums)>k:
            heappop(nums)
        
        return nums[0]
        