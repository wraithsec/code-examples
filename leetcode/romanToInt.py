#!/usr/bin/env python3

#Leet code says it won't work... it does... but its wrong... have to knock out NON VALID ROMAN NUMERALS. 
class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
        
        total = 0
        for i,v in enumerate(s):
            curr_value = numerals.get(v)
            prev_value = numerals.get(s[i - 1]) if i > 0 else 0
            try:
                next_value = numerals.get(s[i + 1])
            except IndexError:
                next_value = 0
            sub = False 

            if curr_value < next_value: continue
            total += (curr_value - prev_value) if curr_value > prev_value else curr_value

        print(s, ":\t", str(total))
        return total
    
Solution().romanToInt('IV')
Solution().romanToInt('MCM')
Solution().romanToInt('LIV')
