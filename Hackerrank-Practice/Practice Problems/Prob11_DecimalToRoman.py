"""
i/p: 8 o/p: VIII

i/p: 43 o/p:XLIII
1	I
4	IV
5	V
9	IX
10	X
40	XL
50	L
90	XC
100	C
400	CD
500	D
900	CM
1000	M
"""

def decToRoman(n):
    st = ""
    rom_st = {1:"I", 4: "IV", 5: "V", 9:"IX", 10:"X", 40:"XL", 50:"L",
                90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    l = []
    while (n != 0):
        for k in rom_st.keys():
            if k<=n:
                l.append(k)
        v = l.pop()
        st += rom_st[v]
        n = n-v

    print (st)

if __name__ == "__main__":
    print ("Enter n")
    n = int(input())
    decToRoman(n)
