def uniqElement(inputArr):
    extra = []
    for i in inputArr:
        if i not in extra:
            extra.append(i)

    print extra


if __name__ == '__main__':
    input = ['a','a','n','n','c','m','m']
    uniqElement(input)