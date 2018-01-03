#coding=utf8
import os
import sys
import codecs
import chardet

abspath = os.path.dirname(sys.argv[0])   
if not os.path.isdir(abspath):
    abspath = sys.path[0]
if not os.path.isdir(abspath):
    abspath = os.path.dirname(__file__)
os.chdir(abspath)
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def printutil(txt):
    encoding = 'utf-8'
    try:
        encoding = chardet.detect(txt).get('encoding')
        # print(encoding)
    except Exception as e:
        # print(e.message)
        pass
    try:
        txt = txt.decode(encoding,'ignore').encode('gbk','ignore')
    except Exception as e:
        print(e.message)
    print(txt)

def writefile(txt, pathfile, mode='w'):
    encoding = 'utf-8'
    try:
        encoding = chardet.detect(txt).get('encoding')
        print(encoding)
    except:
        pass
    with codecs.open(pathfile, mode, 'utf-8') as fr:
        if encoding != 'utf-8':
            txt = txt.decode(encoding, 'ignore').encode('utf-8')
        fr.write(txt)

def readfile(pathfile):
    with codecs.open(pathfile, 'r', 'utf-8') as fr:
        lines = fr.readlines()
    return lines
if __name__ == '__main__':
    s = '哈哈哈'
    # s = s.encode('gbk')
    # print(type(s))
    printutil(s)