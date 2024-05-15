class Solution:
    def romanToInt(self, s: str) -> int:
        lookup  =  {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        N = len (s)
        i = N-1
        output = 0
        while (i>=0):
            if i < N-1 and lookup [s[i]] < lookup [s[i+1]]:
                output -= lookup [s[i]]
            else:
                output += lookup [s[i]]
            i -= 1
        return output


if __name__ == '__main__':
    print(Solution().romanToInt("III")) #3 (Explanation: "III" is III in Roman numerals)  
    print(Solution().romanToInt("IV"))#4 ( Explanation : IV means 4 )
    print(Solution().romanToInt('IX')) #9 (Explanation : IX stands for nine, which is the Roman numeral version of ten.)  
    print(Solution().romanToInt("LVIII"))#58 ( Explanation: L = 50 and V= 5. "LVIII" means 50 + 5 + 3)    
    print(Solution().romanToInt('MCMXCIV')) #1994   (Explanation : M = 1000, CM = 900 , XC = 90 and IV= 4. "MCMXCIV" means 1000 + [M] + 900+[CD])