import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
songs = []
while (True):
    try:
        length, beauty = viread()
        songs.append([beauty, length])
    except EOFError:
        break
songs = sorted(songs)[::-1]

length = songs[0][1]
beauty = songs[0][0]
best_so_far = length * beauty
for i in range(len(songs) - 1):
    _length = songs[i + 1][1]
    _beauty = songs[i + 1][0]
    if best_so_far <= (length + _length) * _beauty:
        best_so_far = (length + _length) * _beauty
        length += _length
        beauty = _beauty
    else:
        break
print(best_so_far)