# coding=utf-8  
""" 
@author: rogerswang  
����tf-idfֵ(��Ƶ ���ĵ�Ƶ��) ��KMeans�ۺ�
��100����Ƶ�ļ�������ɺ��۳�һ��TfIDF_result.txt
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
    #array to save the ��Ƶ
    corpus = []
    
    #��Ϊ100���ɼ��������ļ���
    for i in range(1):
        dir='data/'+str(i)+'/'
        dealfiles(dir, corpus)
    #print len(corpus)
    
    #���ı��еĴ���ת��Ϊ��Ƶ���� ����Ԫ��a[i][j] ��ʾj����i���ı��µĴ�Ƶ
    vectorizer = CountVectorizer()
    #�����ͳ��ÿ�������tf-idfȨֵ
    transformer = TfidfTransformer()
    print len(corpus)
    #print corpus
    #��һ��fit_transform�Ǽ���tf-idf �ڶ���fit_transform�ǽ��ı�תΪ��Ƶ����
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    
    #��ȡģ���е����д���  
    word = vectorizer.get_feature_names()
    
    #��tf-idf�����ȡ������Ԫ��w[i][j]��ʾj����i���ı��е�tf-idfȨ��
    weight = tfidf.toarray()
    
    resName = "TfIDF_result.txt"
    result = codecs.open(resName, 'w', 'utf-8')
    for j in range(len(word)):
        result.write(word[j] + ' ')
    result.write('\r\n\r\n')
    
    #����ÿ���ı���tf-idf����һ��for���������ı����ڶ���for����һ���ı��µĴ���Ȩ��  
    for i in range(len(weight)):
        for j in range(len(word)):
            result.write(str(weight[i][j]) + ' ')
        result.write('\r\n\r\n')
    result.close()
    
    ##�������20�����ĵ�
    print 'caculate the tf-idf completed! And start caculate Kmeans:'
    clf = KMeans(n_clusters=20)
    s = clf.fit(weight)
    print s

    #20�����ĵ�
    print clf.cluster_centers_
    
    separatedclusterfile = 'separatedclusters.txt'
    os.remove(separatedclusterfile)
    sepatedresult = codecs.open(separatedclusterfile, 'a', 'utf-8')
    #ÿ�����������Ĵ�
    print len(clf.labels_)
    i = 1
    while i <= len(clf.labels_):
        #print i, clf.labels_[i-1]
        sepatedresult.write(str(i)+':'+str(clf.labels_[i-1]))
        sepatedresult.write('\r\n')
        i = i + 1
    sepatedresult.close()
	
    #���������صĸ����Ƿ���ʣ�����ԽС˵���طֵ�Խ��
    print(clf.inertia_)
    
    
    