# File Operations in Python

# This operation will override the original 'workfile' with new contents, instead of adding to it
# Detailed file modes:
# r: Read Only
# w: Write Only [will override existing file]
# a: Append a file
# r+: Read and write
# b: Binary mode

f = open('workfile', 'w')
f.write('This is a test \nand another test')
f.close()

f = open('workfile', 'r')
s = f.read()
print(s)
f.close()

f = open('workfile', 'r')
for line in f:
    print(line)
f.close()
