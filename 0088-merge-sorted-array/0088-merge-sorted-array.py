class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Pointers for nums1, nums2, and the end of merged array in nums1
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            print("nums1[p1]", nums1[p1])
            print("nums2[p2]", nums2[p2])
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are elements left in nums2, copy them
        nums1[:p2 + 1] = nums2[:p2 + 1]

solution = Solution()
nums1 = []
nums2 = [1]
solution.merge(nums1, m=0, nums2=nums2, n=1)
print(nums1)  # Should print [1, 2, 3, 4, 5]
