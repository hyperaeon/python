__author__ = 'hzliyong'


import sys
import webbrowser

args = sys.argv[1:]
args.reverse()
print(' '.join(args))
webbrowser.open('http://www.xiupin.com')