def basic_001():
    print 'Twinkle, twinkle, little star,'
    print 'How I wonder what you are!'
    print 'Up above the world so high,'
    print 'Like a diamond in the sky.'
    print 'Twinkle, twinkle, little star,'
    print 'How I wonder what you are'


def hello_001():
    import sys
    print(sys.version)


def what_001():
    import time
    print time


def star_001():
    from math import pi
    r = float(input("Input the radius of the circle : "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))


def I_001():
    Firstname = input('Input your first name: ')
    secondname = input('Input your second name: ')
    print ('Hello ' + Firstname + ' ' + secondname)


def are_001():
    string1 = str(input('Input numpers: '))
    list1 = string1.replace('(', '').replace(')', '').split(', ')
    tuple1 = tuple(list1)
    print('List: {}'.format(list1))
    print('Tuple: {}'.format(str(tuple1)))
    # print "list1[1:24]: ", list1[1:4]


def java_001():
    filename = input('Input a filename: ')
    filename1 = filename.split('.')
    print ('The extesion from the filename is: ' + repr(filename1[-1]))


def colors_001():
    color_list = ["Red", "Green", "White", "Black"]
    print (color_list[0], color_list[1])


def exam_001():
    exam_st_date = (11, 12, 2014)
    print ('The examination will start from : ' + str(exam_st_date[0]) + '/' + str(exam_st_date[1]) + '/' + str(
        exam_st_date[2]))


def n_001():
    n = (5)
    nn = (55)
    nnn = (555)
    print (n + nn + nnn)


def calender_001():
    import calendar
    y = int(input("Input the year : "))
    m = int(input("Input the month : "))
    print(calendar.month(y, m))


def document_001():
    print 'This'
    print 'is a ....... multi-line'
    print 'heredoc string --------> example'


def date_001():
    from datetime import date

    date2 = date(2014, 7, 2)
    date1 = date(2014, 7, 11)
    delta = date1 - date2
    print(delta.days)


def difference_001():
    pi = 3.1415926535897931
    r = 6
    V = pi * (r * r)
    print V


def fly_001():
    number3 = input('Say a number: ')

    if number3 <= 17:
        return 17 - number3
    else:
        return (number3 - 17) * 2


def numbers_002():
    zalen = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]

    for n in zalen:
        if n == 248:
            break
        elif n % 2 == 0:
            print(n)


def colors_002():
    color_list_3 = set(["White", "Black", "Red"])
    color_list_4 = set(["Red", "Green"])

    print(color_list_3.difference(color_list_4))


def dreieck_001():
    a = int(input("Input the base : "))
    b = int(input("Input the height : "))
    area = a * b / 2
    print("area = ", area)


def rechnen():
    x = input('Input a number: ')
    y = input('Input a number: ')
    z = input('Input a number: ')
    if x == y or x == z or y == z:
        summe = 0
    else:
        summe = x + y + z
    print(summe)


def rechnen_001():
    m = input('input a number: ')
    f = input('input a second number: ')
    if m + f == 15 or 16 or 17 or 18 or 19 or 20:
        ergebnis = m + f - 20
    else:
        ergebnis = m + f
    print(ergebnis)


def lengen_001():
    str = "this is string example....wow!!!";
    print "Length of the string: ", len(str)


def anzahl_001():
    w = raw_input('Gife me a word: ')
    anzahl = len(w)
    print anzahl


def ing_001():
    user_input = raw_input("What's your favourite language? ")
    print("My favourite language is " + user_input)


def sortiren_001():
    items = raw_input("Input comma separated sequence of words")
    words = [word for word in items.split(",")]
    print(",".join(sorted(list(set(words)))))


def hello_002():
    add_tags = ('i', 'Python') == '<i>Python</i>'
    print (add_tags)


def hello_003():
    insert_end = ('Python') == 'onononon'
    print (insert_end)


def hello_004():
    print ('''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*''')


def hello_005():
    n = 15
    sternchen = ''
    for k in range(0, n):
        sternchen += '*'

    zeile = 0
    anzahl = 0
    direction = 1
    while zeile < n:
        zeile += 1
        if anzahl > n/2:
            direction = 0

        if direction == 1:
            anzahl += 1
        else:
            anzahl -= 1

        print (sternchen[0:anzahl])


def hello_006():
    a = dict()
    for n in range(1, 16):
        a [n] = n ** 2
    print(a)


def hello_007():
    normal = {0: 10, 1: 20}
    normal.update({2: 30})
    print normal


def hello_008():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dic1.update(dic2)
    dic1.update(dic3)
    print dic1


def hello_009():
    dict = {1: 10, 2: 20}
    numer = input('Say me the number to check')
    if numer in dict.keys():
        print ('input number is in the dicternary')
    else:
        print ('input number is not in the dicternary')


def hello_010_():
    dicternary = {1: 10, 2: 20}
    print dicternary
    for k,v in dicternary.iteritems():
        print(k,v)


def hello_011():
    n = 10
    squares = {}
    for k in range(1, n + 1):
        squares[k] = k * k

    print squares


def hello_011_():
    n = 5
    squares = {k: k*k for k in range(1, n+1)}

    print squares

if __name__ == '__main__':
    # basic_001()
    # hello_001()
    # what_001()
    # star_001()
    # I_001()
    # are_001()
    #  java_001()
    #  colors_001()
    # exam_001()
    # n_001()
    # calender_001()
    # document_001()
    # date_001()
    # difference_001()
    # fly_001()
    # numbers_002()
    # colors_002()
    # dreieck_001()
    # rechnen()
    # rechnen_001()
    # lengen_001()
    # anzahl_001()
    # ing_001()
    # sortiren_001()
    # hello_002()
    # hello_003()
    # hello_004()
    #hello_005()
    #hello_006()
    #hello_007()
    #hello_008()
    #hello_009()
    # hello_010_()
    hello_011()
    hello_011_()