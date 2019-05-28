class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return True


    def comparator(a, b):
        if a<b:
            return -1
        elif a == b:
            return 0
        else: return 1

        print "nothing"


if __name__ == "__main__":

    n = int(raw_input())
    data = []
    for i in range(n):
        name, score = raw_input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, cmp=Player.comparator)
    for i in data:
        print i.name, i.score
