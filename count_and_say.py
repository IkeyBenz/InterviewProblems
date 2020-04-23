'''
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers with the first five terms as following:
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

'''


class Solution:
    def split_by_change(self, s: str) -> [str]:
        splits = [s[0]]
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                splits[-1] += s[i+1]
            else:
                splits.append(s[i+1])
        return splits

    def countAndSay(self, n: int) -> str:
        last = '1'
        for _ in range(n-1):
            splits = self.split_by_change(last)
            new = ''
            for split in splits:
                new += str(len(split)) + split[0]
            last = new
        return last


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))  # 1
    print(s.countAndSay(2))  # 11
    print(s.countAndSay(3))  # 21
    print(s.countAndSay(4))  # 1211
    print(s.countAndSay(5))  # 111221
