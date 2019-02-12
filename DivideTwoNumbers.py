__author__="Vishal Garg"
#Divice two numbers without using multiplication, + and - opertors

class DivideTwoNumbers(object):
    def divideTwoNumber(self,dividend, divisor):
        sum = 0
        count = -1
        reminder = 0
        while sum <= dividend:
            sum = sum + divisor
            count += 1
        reminder = dividend - (count * divisor)
        print "Reminder:",reminder
        return count

if __name__=='__main__':
    obj = DivideTwoNumbers()
    print obj.divideTwoNumber(7,2)


