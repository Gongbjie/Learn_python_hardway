#!/usr/bin/python

from sys import argv

script, filename = argv

txt = open(filename)

print "filename %r" % filename
print "file content:\n%s" % txt.read()
txt.close()