class Solution:
    # Binary Search in python
    def binarySearch(s, array, x, low, high):
        # Repeat until the pointers low and high meet each other
        while low <= high:
            mid = low + (high - low)//2
            if array[mid] == x:
                return mid
            elif array[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def binarySearch2(s, array, x, low, high):
        # Repeat until the pointers low and high meet each other
        while low <= high:
            mid = low + (high - low)//2
            if array[mid] == x:
                return mid
            elif array[mid] > x:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        prv = -1000
        count = 0
        for i in A:
            if prv < i:
                prv = i
                count += 1
            else:
                break
        ele = self.binarySearch(A[0:count], B, 0, len(A[0:count])-1)
        if ele == -1:
            x = self.binarySearch2(A[count:], B, 0, len(A[count:])-1)
            if x == -1:
                return -1
            else:
                return count+x
        return ele


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40,
     39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]
B = 1
z = Solution()
u = z.solve(A, B)
print(u)
