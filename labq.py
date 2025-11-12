with open("sport.txt", "r", encoding="cp1251") as file:
    content = file.read()
    k = []
    cnt = 0
    for a in content.split('\t'):
        if cnt%6==0 and cnt!=0:
            b, c = a.split('\n')
            k.append(b)
            k.append(c)
        else:
            k.append(a)
        cnt+=1
i = 0
sport_spisok = {}
while i < len(k):

    if (i - 3) % 7 == 0 and i >= 3:
        sports = [x.strip() for x in k[i].split(',')]

        for sport in sports:
            if sport != '':
                if sport in sport_spisok:
                    sport_spisok[sport] += 1
                else:
                    sport_spisok[sport] = 1
    i += 1
genexp = [(z, sport_spisok[z]) for z in sorted(sport_spisok, key=sport_spisok.get, reverse=True)]
print(genexp[0], genexp[1], genexp[2])