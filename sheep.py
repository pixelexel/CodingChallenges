T = int(raw_input())

final = []

for i in range(T):

    c = 2

    n = int(raw_input())



    a = []

    w = n

    while True:

        if w == 0:
            final.append(0)
            break

        b = set(str(w))

        for d in b:
            if int(d) not in a:
                a.append(int(d))

        if len(a) == 10:
            final.append(w)
            break

        w = n*c
        c += 1


for i in range(T):
        if final[i] == 0:
            print "Case #%d: INSOMNIA" %(i+1)
        else:
            print "Case #%d: %d" %(i+1,final[i])
