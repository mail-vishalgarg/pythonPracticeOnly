def reverseNum(inputNum):
    res = 0
    rev = 0
    while inputNum > res:
        res = inputNum / 10
        rev = rev + (res * 10)


if __name__ == '__main__':
    reverseNum(1234)


