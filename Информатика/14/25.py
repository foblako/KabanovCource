for x in "0123456789abcdefghijk":
    for y in "0123456789abcdefghijk":
        a = int(f"12{y}{x}9", 21) + int(f"36{y}99", 21)
        if a % 18 == 0:
            print(a / 18, x, y)
