from files import *

try:
    arq = open('cursoemvideo.txt', 'r+')
except FileNotFoundError:
    arq = open('cursoemvideo.txt', 'w+')
else:
    arq.close()