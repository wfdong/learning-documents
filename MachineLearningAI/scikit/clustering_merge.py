# coding=utf-8  
""" 
@author: rogerswang  
�ϲ�ʵ�����ƺ;�����
"""  
import os  
import sys
import codecs
import shutil


records=[]

if __name__ == "__main__":
    #����������ļ��Ļ�������Ҫ�Ķ�һ��
    source1 = open("data/0/respath/result.txt",'r')
    source2 = open("separatedclusters.txt",'r')
    
    shutil.rmtree("result/", True)
    os.makedirs("result/")
    
    
    for line in source1:
        if line!='':
            records.append(line) 
                
    for line in source2:
        #print line
        if line!='' and len(line.split(':'))==2:
            #print line
            lUinNO = line.split(':')[0]
            cluster = line.split(':')[1]
            resName = 'result/'+str(cluster)+'.txt'
            result = codecs.open(resName, 'a', 'utf-8')
            #print int(lUinNO)-1
            lUinInfo = records[int(lUinNO)-1]
            #print lUinInfo
            if lUinInfo!='' and lUinInfo.split(' ')[0]!='':
                lUin = lUinInfo.split(' ')[0]
                result.write(lUin)
                result.write('\r\n')
        
