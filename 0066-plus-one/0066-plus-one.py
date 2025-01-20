class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Increment the last digit by 1
        digits[len(digits) - 1] += 1

        # Traverse the list in reverse to handle carries
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:  # If the digit equals 10, handle the carry
                digits[i] = 0  # Reset the current digit to 0
                if i == 0:  # If it's the most significant digit
                    digits.insert(0, 1)  # Insert 1 at the beginning of the list
                else:
                    digits[i - 1] += 1  # Add carry to the previous digit

        return digits  # Return the updated list


        