# coding=utf-8  
""" 
@author: rogerswang  
计算tf-idf值(词频 逆文档频率) 和KMeans聚合
将100个词频文件计算完成后汇聚成一个TfIDF_result.txt
"""  
  
import time          
import re          
import os  
import sys
import codecs
import shutil
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans


def dealfiles(dir, corpus):
    if os.path.isfile(dir+'/respath/result.txt'):
        content = open(dir+'/respath/result.txt', 'r')
        for line in content:
            #if line!="" and len(line.split(':'))==2:
                #lUin = str(line).split(':')[0]
                #tmpcontent = str(line).split(':')[1]
                #corpus.append(lUin+u' :{')
                #for tmp in tmpcontent.split(' '):
                #    corpus.append(tmp.strip())
                #    corpus.append(' ')
                #print line
                ##corpus.append(unicode(line.strip(),errors='ignore'))
                #corpus.append(lUin+' ')
            corpus.append(line.strip())
        #corpus.append('},')
        content.close()

if __name__ == "__main__":
    #array to save the 词频
    corpus = []
    
    #改为100即可计算所有文件的
    for i in range(1):
        dir='data/'+str(i)+'/'
        dealfiles(dir, corpus)
    #print len(corpus)
    
    #将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
    #该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
    print len(corpus)
    #print corpus
    #第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    
    #获取模型中的所有词语  
    word = vectorizer.get_feature_names()
    
    #将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()
    
    resName = "TfIDF_result.txt"
    result = codecs.open(resName, 'w', 'utf-8')
    for j in range(len(word)):
        result.write(word[j] + ' ')
    result.write('\r\n\r\n')
    
    #计算每个文本的tf-idf，第一个for遍历所有文本，第二个for遍历一个文本下的词语权重  
    for i in range(len(weight)):
        for j in range(len(word)):
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')
    result.close()
    
    ##这里假设20个中心点
    print 'caculate the tf-idf completed! And start caculate Kmeans:'
    clf = KMeans(n_clusters=20)
    s = clf.fit(weight)
    print s

    #20个中心点
    print clf.cluster_centers_
    
    separatedclusterfile = 'separatedclusters.txt'
    os.remove(separatedclusterfile)
    sepatedresult = codecs.open(separatedclusterfile, 'a', 'utf-8')
    #每个样本所属的簇
    print len(clf.labels_)
    i = 1
    while i <= len(clf.labels_):
        #print i, clf.labels_[i-1]
        sepatedresult.write(str(i)+':'+str(clf.labels_[i-1]))
        sepatedresult.write('\r\n')
        i = i + 1
    sepatedresult.close()
	
    #用来评估簇的个数是否合适，距离越小说明簇分的越好
    print(clf.inertia_)
    
    
    