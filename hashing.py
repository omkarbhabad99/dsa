"""
Problem Description

Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.

Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return_val = -1

        dt = {}
        final_min = float('inf')
        temp = float('inf')
        flag = 0

        for i in range(len(A)):
            if A[i] not in dt:
                dt[A[i]] = i
            else: 
                temp = i - dt[A[i]]
                final_min = min(final_min, temp)
                dt[A[i]] = i  
                flag = 1  

        if flag == 0:
            return -1
        else:
            return final_min



"""
Problem Description

Given a 2D array A of integer points on a 2D plane. Find and return the number of unique points in the array.
The ith point in the array is (A[i][0], A[i][1])
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        dt = {}
        n = len(A)

        for i in range(n):
            point = tuple(A[i])

            if point not in dt:
                dt[point] = 1
            else:
                dt[point] += 1

        return len(dt)