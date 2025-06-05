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
