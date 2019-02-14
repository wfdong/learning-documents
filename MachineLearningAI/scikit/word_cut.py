#encoding=utf-8
""" 
@author: rogerswang  
对每个文件做分词处理，每个目录的用户数据形成一个result文件，
其中的每一行是一个用户的分词数据
处理完成后汇聚成100个词频文件
"""  

import sys
import re
import codecs
import os
import shutil
import jieba
import jieba.analyse

#导入自定义FIFA词典
jieba.load_userdict("fifa_dict.txt")

def dealfiles(dir, resName):
    result = codecs.open(resName, 'a', 'utf-8')
    for file in os.listdir(dir):
        if os.path.isfile(dir+'/'+file):
            content = open(dir+'/'+file, 'r')
            lUin = str(file).split('.')[0]
            result.write(lUin+'  ')
            for line in content:
                line = line.rstrip('\r\n')
                if line!="":
                    #line = unicode(line, errors='ignore')
                    #print line
                    #精确模式,cut_all 参数用来控制是否采用全模式
                    seglist = jieba.cut(line,cut_all=False)
                    #seglist = jieba.cut(line)
                    #.replace('\n', ' ')
                    output = ' '.join(list(seglist))
                    result.write(output + ' ')
            content.close()
        result.write('\r\n')
    result.close()

#Read file and cut
def word_cut():
    for i in range(100):
        dir='data/'+str(i)+'/'
        respath = dir+'/respath/'
        if os.path.isdir(respath):
            shutil.rmtree(respath, True)
        os.makedirs(respath)
        resName = respath+'/result.txt'
        if os.path.exists(resName):
            os.remove(resName)
        dealfiles(dir, resName)


#Run function
if __name__ == '__main__':
    word_cut()
