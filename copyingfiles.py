from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "copying from %s to %s" %(from_file,to_file)

#we could do this two on one line too. how?

in_file=open(from_file)
indata=in_file.read()

print "the input file is %d bytes long"%len(indata)

print "does the output file exist? %r"%exists(to_file)

print "ready . Hit return and continue
