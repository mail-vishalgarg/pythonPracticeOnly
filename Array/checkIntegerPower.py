class integerPower(object):
    def isValidPower(self,num, target):
        if target == 0:
            return False

        pow = 1
        while pow < num:
            pow = pow * target
            if pow == num:
                return True


if __name__ == '__main__':
    power = integerPower()
    print power.isValidPower(27,3)
