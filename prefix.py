class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        pf_sum = [0] * (A+1)

        for i in range(len(B)):
            start_index = B[i][0] - 1
            end_index = B[i][1]
            value = B[i][2]

            pf_sum[start_index] += value

            if end_index < A:
                pf_sum[end_index] -= value

        ans = [0] * A
        ans[0] = pf_sum[0]

        for i in range(1, A):
            ans[i] = ans[i-1] + pf_sum[i]
        
        return ans





# Problem Description

# Kamal is a software developer and he's working on a new feature for an e-commerce website. The website has a list of prices for different products, and Kamal needs to find the maximum price of all products up to a given index.

# He has the list of prices in an array A of length N, and he needs to write a program that will return the maximum price occurring in the subarray from 0 to i for every index i. Kamal needs your help to implement this function.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        ans.append(A[0])

        for i in range(1,len(A)):

            if A[i] > ans[i-1]:
                ans.append(A[i])
            else:
                ans.append(ans[i-1])

        return ans
