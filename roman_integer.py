class Solution:
    key = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        answer = 0

        skip_next = False
        for i in range(len(s) - 1):
            if skip_next:
                skip_next = False
                continue

            if s[i] in ['I', 'X', 'C'] and s[i:i+2] in Solution.key:
                answer += Solution.key[s[i:i+2]]
                skip_next = True
                continue

            answer += Solution.key[s[i]]

        if not skip_next:
            answer += Solution.key[s[-1]]

        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))  # 3
    print(s.romanToInt('IV'))  # 4
    print(s.romanToInt('IX'))  # 9
    print(s.romanToInt('LVIII'))  # 58
    print(s.romanToInt('MCMXCIV'))  # 1994
