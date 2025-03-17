class Solution(object):
    def romanToInt(roman):
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        for char in roman:
            if char not in map:
                raise TypeError(f"Invalid character '{char}' in Roman numeral")

        invalid_sequences = ["VV", "LL", "DD", "IIII", "XXXX", "CCCC", "MMMM"]
        for seq in invalid_sequences:
            if seq in roman:
                raise ValueError(f"Invalid sequence '{seq}' in Roman numeral")

        convertedNumber = 0
        for i in range(len(roman)):
            currentNumber = map.get(roman[i])
            nextNumber = map.get(roman[i + 1]) if i + 1 < len(roman) else 0
            if currentNumber >= nextNumber:
                convertedNumber += currentNumber
            else:
                convertedNumber -= currentNumber
                
        return convertedNumber