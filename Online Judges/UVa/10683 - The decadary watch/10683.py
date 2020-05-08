while True:
    try:
        time = int(input().strip())
        h = time // 1000000
        time = time % 1000000
        m = time // 10000
        time = time % 10000
        s = time // 100
        time = time % 100
        ms = (((3600 * h) + (60 * m) + s) * 100) + time
        h = ms // 86400
        ms = ms % 86400
        m = ms // 864
        ms = ms % 864
        s = ms // (864 / 100) 
        ms = ms % (864 / 100)
        ms = int(ms * 864 / )
        print(f"{h:02}{m:02}{s:02}{ms:02}")
    except EOFError:
        break