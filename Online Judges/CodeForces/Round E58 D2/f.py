num_cities, num_trucks = [int(x) for x in input().split()]
cities = [int(x) for x in input().split()]
ans = 0
for i in range(num_trucks):
    s, f, c, r = [int(x) for x in input().split()]
    if r == 0:
        ans = max(ans, c * (cities[f - 1] - cities[s - 1]))
    if 