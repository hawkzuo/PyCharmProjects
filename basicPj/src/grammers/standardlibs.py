import os

print(os.listdir(os.curdir))
os.mkdir('dummydir')
os.rename('dummydir', 'foodir')
os.rmdir('foodir')
# print(os.system('dir'))    not formatting well
print(os.environ['PYTHONPATH'])
print(os.getenv('PYTHONPATH'))
# High-level operations :   shutil.rmtree/move/copy;     glob.glob


import sys
if __name__ == '__main__':
    print(sys.platform)
    print(sys.version)
    print(sys.prefix)
    print(sys.path)
