dp = []
for i in range(1005):
    dp.append((i // 5) + (i % 5) // 2 + (i % 5) % 2)

for n in range(int(input().strip())):
    freq = {}
    _, l = input(), [int(x) for x in input().strip().split()]
    m = min(l)
    for i in l:
        if i - m in freq:
            freq[i - m] += 1
        else:
            freq[i - m] = 1
    ans0 = 0
    ans1 = 0
    ans2 = 0
    ans3 = 0
    ans4 = 0
    for i in freq:
        ans0 += dp[i] * freq[i]
        ans1 += dp[i + 1] * freq[i]
        ans2 += dp[i + 2] * freq[i]
        ans3 += dp[i + 3] * freq[i]
        ans4 += dp[i + 4] * freq[i]
    print(min([ans0, ans1, ans2, ans3, ans4]))
