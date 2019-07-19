def expandStr(st, pos):
    i = 0
    exp = ""
    while i < len(st):
        if (ord(st[i]) >= ord("a") and ord(st[i]) <= ord("z")):
            exp += st[i]
            i += 1
        elif (ord(st[i]) >= 48 and ord(st[i]) <= 57):
            freq = int(st[i])

            for _ in range(1, freq):
                exp += st[i-1]
            i += 1

    print (exp)
    print (exp[pos])


if __name__ == "__main__":
    st = input()
    pos = int(input())
    expandStr(st, pos)
