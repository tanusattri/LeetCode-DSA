class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD= 10**9 + 7
        n= len(s)
        pow10= [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i]=(pow10[i- 1]* 10) % MOD
        pref_sum= [0]*(n+1)     
        pref_x= [0]*(n+1)        
        non_zero_count= [0]*(n + 1) 
        for i in range(n):
            digit= int(s[i])
            pref_sum[i + 1]= pref_sum[i] + digit
            if digit!= 0:
                pref_x[i + 1]= (pref_x[i] * 10 + digit) % MOD
                non_zero_count[i + 1] = non_zero_count[i] + 1
            else:
                pref_x[i + 1] =pref_x[i]
                non_zero_count[i + 1] = non_zero_count[i]
        ans = []
        for l, r in queries:
            current_sum = pref_sum[r + 1] - pref_sum[l]
            k = non_zero_count[r + 1] - non_zero_count[l]
            if k == 0:
                ans.append(0)
                continue
            x = (pref_x[r + 1] - pref_x[l] * pow10[k]) % MOD
            ans.append((x * current_sum) % MOD)
        return ans