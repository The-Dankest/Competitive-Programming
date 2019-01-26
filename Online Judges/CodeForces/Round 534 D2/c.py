vert_ans = ["1 1", "3 1"]
vert_num = 0
horz_ans = ["1 3", "2 3", "3 3", "4 3"]
horz_num = 0
for c in input():
    if c == "0":
        print(vert_ans[vert_num % 2])
        vert_num += 1
    else:
        print(horz_ans[horz_num % 4])
        horz_num += 1
