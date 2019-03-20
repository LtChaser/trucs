import time

def bullshit():
    x = True
    meprint = "* *****"
    meprint2 = "*    *   **** *"
    meprint3 = "*    ****    *        *"
    while x < True:
        for i in meprint:
            time.sleep(0.1)
            print(meprint)
            print(meprint2)
            print(meprint3)
            meprint = '*  **  * ' + meprint
            meprint2 = '* * ' + meprint2
            meprint3 = '*   ***      *    *****     * ' + meprint3
            meprint4 = meprint + meprint2 + meprint3
            print("* \n * \n * \n *")
            print(meprint4)
            x += 1
    # print(meprint)
    # print("Lenghth is " + str(len(meprint)))

def another_bl():
    x = True
    s = "*                                                                           *"
    while x:
        time.sleep(0.1)
        s = s[1:]
        print(s)
        print(len(s))
        if len(s) == 50:
            break

def meheart():
    i = 15
    y = 30
    x = 0
    z = 15
    h = '*'
    w = ' '
    while i > 0:
        time.sleep(0.2)

        print(w*i + h + w*x + h)
        i -= 1
        x += 2

def mecircle():
    i = 32
    t = 16

    x = 30
    y = 0
    s = "*"
    w = " "
    z = 15
    v = 30
    while i > 0:
        if x > 15:
            time.sleep( 0.1)
            print(w*x + s + w*y + s)
        elif x == 15:
            while t > 0:
                print(w * (t) + s + w * (y-7) + s)
                t += 1
        elif x < 15:
            time.sleep(0.1)
            print(w*z + s + w*v + s)
            z += 1
            v -= 2
        x -= 1
        y += 2
        i -= 1
mecircle()