# roman to int 
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        arr = []
        for i in s:
            arr.append(d.get(i))
        i = len(arr)-1
        # print(arr[i-1])
        while True:
            if(i == 0):
                break
            if(arr[i] > arr[i-1]):
                arr[i-1] = arr[i-1]*-1
            i = i-1
        s = 0
        for i in arr:
            s = s+i
        return s


A = Solution()
A.romanToInt("MCMXCIV")
A.romanToInt("VII")
# "III"
# "LVIII"
# "MCMXCIV"
