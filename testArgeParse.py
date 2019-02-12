import argparse
parser = argparse.ArgumentParser(description='Add your description here')
parser.add_argument('-i','--input',help='Input the file name',required=True)
parser.add_argument('-o','--output',help='output the file name',required=True)
args = parser.parse_args()

print ("Input file: %s " % args.input)
print ("output file: %s " % args.output)