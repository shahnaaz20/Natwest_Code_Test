def nonDivisibleSubset(k,s):
    remainder_list = []
    for num in s:
        remainder_list.append(num % k)
    count = 0
    for i in range(k//2 + 1):
        if i in remainder_list or k - i in remainder_list:  
            if i * 2 % k == 0:
                count += 1
            else:
                count += max(remainder_list.count(i), remainder_list.count(k-i))
    return count
    
n, k = map(int, input().split())
s = list(map(int, input().split()[:n]))
print(nonDivisibleSubset(k,s))