class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calculate_waviness(number: str) -> int:
            waviness = 0
            n = len(number)
            
            # Only numbers with at least 3 digits can have peaks/valleys
            if n < 3:
                return 0
            
            for i in range(1, n - 1):
                left_neighbor = int(number[i-1])
                current_digit = int(number[i])
                right_neighbor = int(number[i+1])
                
                # Check peak condition
                if (current_digit > left_neighbor and 
                    current_digit > right_neighbor):
                    waviness += 1
                
                # Check valley condition
                elif (current_digit < left_neighbor and 
                    current_digit < right_neighbor):
                    waviness += 1
            
            return waviness

        total_waviness = sum(calculate_waviness(str(num)) for num in range(num1, num2 + 1))
        
        return total_waviness
