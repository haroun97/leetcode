# Intuition
# The problem asks to merge two sorted arrays, nums1 and nums2, into nums1, 
# where nums1 has enough space to hold both arrays. 
# The most efficient way to merge them is to start from the end of nums1 and nums2 
# and fill nums1 from the back to avoid overwriting any elements.

# Approach
# 1. Initialize three pointers: p1 for the last element of the first part of nums1 (m - 1),
#    p2 for the last element of nums2 (n - 1), and p for the last index of nums1 (m + n - 1).
# 2. Compare the elements of nums1[p1] and nums2[p2] in reverse order.
#    - If nums1[p1] is greater, place nums1[p1] at the position p in nums1 and move p1 left.
#    - Otherwise, place nums2[p2] at position p in nums1 and move p2 left.
# 3. Once either p1 or p2 reaches -1, if any elements remain in nums2, 
#    copy them into nums1.
# 4. No need to copy the remaining elements in nums1, as they are already in place.

# Complexity
# - Time complexity: O(m + n)
#   We only iterate through each element in nums1 and nums2 once, so the time complexity is linear in the size of the input arrays.
# - Space complexity: O(1)
#   Since the merging is done in-place in nums1, no extra space is used other than the input arrays.

# Code
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Pointers for nums1, nums2, and the end of merged array in nums1
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            # Print the current elements being compared for debugging purposes
            print("nums1[p1]", nums1[p1])
            print("nums2[p2]", nums2[p2])
            
            # If current element in nums1 is greater, place it at the end of nums1
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1  # Move pointer p1 to the left
            else:
                # If current element in nums2 is greater, place it at the end of nums1
                nums1[p] = nums2[p2]
                p2 -= 1  # Move pointer p2 to the left
            p -= 1  # Move the pointer p in nums1 to the left

        # If there are any remaining elements in nums2, copy them to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]  # Copy any leftover elements from nums2

# Example usage
solution = Solution()
nums1 = [0, 0, 0, 0, 0]  # Make sure nums1 has enough space
nums2 = [1, 2, 3, 4, 5]
solution.merge(nums1, m=0, nums2=nums2, n=5)
print(nums1)  # Should print [1, 2, 3, 4, 5]
