class Solution:
    def splitnum(self, n: int) -> list:
        l = []
        while n != 0:
            rem = int(n % 10)
            n = int(n/10)
            l.append(rem*rem)
        print(l)
        return l

    def isHappy(self, n: int) -> bool:
        m = {}
        l = 0
        count = 10000
        while True:
            nums = self.splitnum(n)
            n = sum(nums)
            if m.get(n) or count == 0:
                # the number looop
                # print(m)
                return False
            else:
                m[n] = -1
            count -= 1

            if n == 1:
                return True


a = Solution()

x = a.isHappy(19)
