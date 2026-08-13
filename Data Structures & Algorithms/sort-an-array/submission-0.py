class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: arrays with 0 or 1 element are already sorted
        if len(nums) <= 1:
            return nums

        # 1. Divide: Find the middle point
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # 2. Conquer: Recursively sort both halves
        sorted_left = self.sortArray(left_half)
        sorted_right = self.sortArray(right_half)

        # 3. Combine: Merge the sorted halves
        return merge(sorted_left, sorted_right)



def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements from both sub-arrays and merge them in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append any remaining elements from left or right sub-arrays
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array