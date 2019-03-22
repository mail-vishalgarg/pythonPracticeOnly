import sys, getopt

ifile = ''
ofile = ''
try:
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
except getopt.GetoptError as e:
    print (str(e))
    print ("usage:%s -i input -o output" % sys.argv[0])
    sys.exit(2)
# print 'myopts:',myopts
# print 'aaaaa: args: ', args
for o,a in myopts:
    if o == '-i':
        ifile = a
    elif o == '-o':
        ofile = a
    else:
        print ("usage:%s -i input -o output" % sys.argv[0])

print ("Input file: %s and output file: %s" % (ifile,ofile))