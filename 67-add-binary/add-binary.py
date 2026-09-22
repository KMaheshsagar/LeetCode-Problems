class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)
      
        # Convert binary string 'b' to integer (base 2)
        decimal_b = int(b, 2)
      
        # Add the two decimal numbers
        decimal_sum = decimal_a + decimal_b
      
        # Convert the sum back to binary string
        # bin() returns format like '0b101', so we slice from index 2
        binary_result = bin(decimal_sum)[2:]
        return binary_result
      