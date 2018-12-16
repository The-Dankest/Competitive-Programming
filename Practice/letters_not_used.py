[print("Letters missing in case #{}: {}".format(i + 1, "".join(sorted(set("abcdefghijklmnopqrstuvwxyz") - set(input().lower()))))) for i in range(int(input()))]
