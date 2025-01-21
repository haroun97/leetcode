# Intuition
# The task is to add two binary strings. Binary addition is similar to decimal addition, 
# but it operates on base-2. We add corresponding digits from right to left, 
# keeping track of the carry for each addition.

# Approach
# 1. Use two pointers to iterate over the binary strings `a` and `b` from the last character 
#    (least significant bit) to the first character (most significant bit).
# 2. Initialize a `carry` variable to store the carry from the previous addition.
# 3. Add the corresponding digits from `a` and `b`, along with the carry.
# 4. Append the remainder (modulo 2) to the result and update the carry (integer division by 2).
# 5. If a carry remains after processing all digits, append it to the result.
# 6. Reverse the result list and convert it to a string before returning.

# Complexity
# - Time complexity: O(max(len(a), len(b)))
#   Each character in `a` and `b` is processed once.
# - Space complexity: O(max(len(a), len(b)))
#   The result list stores up to max(len(a), len(b)) characters.

# Code
class Solution: 
    def addBinary(self, a: str, b: str) -> str:
        # Initialize carry to store the carry from the previous operation
        carry = 0
        # Result list to store the binary digits of the sum
        res = []
        
        # Pointers to traverse the strings a and b from right to left
        idxA, idxB = len(a) - 1, len(b) - 1
        
        # Process each digit in a and b, including the carry
        while idxA >= 0 or idxB >= 0 or carry == 1:
            # Add the current digit from string a to carry if idxA is valid
            if idxA >= 0:
                carry += int(a[idxA])  # Convert binary digit to integer
                idxA -= 1  # Move the pointer to the left
            
            # Add the current digit from string b to carry if idxB is valid
            if idxB >= 0:
                carry += int(b[idxB])  # Convert binary digit to integer
                idxB -= 1  # Move the pointer to the left

            # Append the current binary digit (carry % 2) to the result
            res.append(str(carry % 2))
            # Update carry for the next iteration (carry // 2)
            carry = carry // 2
        
        # Join the reversed result list into a string and return
        return "".join(res[::-1])
