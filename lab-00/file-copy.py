#!/usr/bin/python

f = open("/var/log/system.log")
buf = f.read()
print buf
f1 = open("mylogfile.log")
f1.write(buf)
f1.close()