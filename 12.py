# palindromic 
class Solution:
    # @param A : string
    # @return an integer
    
    def addtime(self, time, mins):
        time[1] = time[1]+mins
        if(time[1] > 59):
            hrs = time[1]/60
            time[1] = time[1]-int(hrs)*60
            time[0] = time[0]+int(hrs)
            if(time[0] > 23):
                extra = time[0]/24
                time[0] = time[0]-24*hrs
        return time

    def ispal(self, time):
        num = time[1]
        # rev num
        rem = num % 10
        num = rem*10+int(num/10)
        if num == time[0]:
            return True
        else:
            return False

    def solve(self, A):
        A = A.split(":")
        A = [int(A[0]), int(A[1])]
        count = 0
        while True:
            temp = self.addtime(A[:], count)
            if self.ispal(temp[:]):
                print(count)
                return count
            count += 1

a = Solution()
a.solve("10:10")
