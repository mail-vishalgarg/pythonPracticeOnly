class LengthOfLastWord(object):
    def lenghtOfLastWord(self, s):
        lastIndexOfSpace = s.rfind(' ')
        length_of_last_word = s[lastIndexOfSpace + 1:]
        print 'Length of the last word:',len(length_of_last_word)

if __name__ == '__main__':
    input_str = 'test only please ignore'
    obj = LengthOfLastWord()
    obj.lenghtOfLastWord(input_str)