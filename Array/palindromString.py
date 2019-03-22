def palindromString(str):
    print "reverse string:",str[::-1]
    if str == str[::-1]:
        print "palindrom"
    else:
        print "not a palindrom"


def palindromString2(str):
    revStr = ''
    i = len(str)
    while i > 0:
        revStr = revStr + str[i -1]
        i = i -  1

    print 'rev str:',revStr
    if revStr == str:
        print "palindrom"
    else:
        print 'not a palindrom'

if __name__ == '__main__':
    str = 'abcd'
    palindromString(str)
    palindromString2(str)