#!/usr/bin/env python3
file_String = open("/tmp/String.txt")
digist = ""
for i in file_String.read():
    if i.isdigit():
        digist += i
print(digist)
