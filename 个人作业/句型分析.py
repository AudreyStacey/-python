from multiprocessing import  Process
from concurrent.futures import  ProcessPoolExecutor
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
import numpy as np
import csv
import pandas as pd
from snownlp import SnowNLP

def duqu(filename): #读取文件
   with open(filename,'r',encoding='utf-8') as f:
      en=f.read()
   return en

def en_chouqu(file):#抽取英文句子
   en_text=sent_tokenize(file)[0:5000]#抽取5000个句子
   return en_text

def zh_chouqu(file):#抽取中文句子
   zh_text=SnowNLP(file).sentences[0:5000]
   return zh_text

def en_whattype(a): #判断句型
   if (a[0][0]=="there") and (a[1][0]=="is" or a[1][0]=="are") and (a[-1][0]=="."):
        return "there be句型"
   elif a[-1][0]==".":
        return "陈述句"
   elif (a[0][0]=="what"or a[0][0]=="when"or a[0][0]=="which"or a[0][0]=="who"or a[0][0]=="where") and (a[-1][0]=="?"):
        return "特殊疑问句"
   elif (a[0][0]=="did"or a[0][0]=="do"or a[0][0]=="does"or a[0][0]=="had"or a[0][0]=="has"or a[0][0]=="how"or a[0][0]=="is" or a[0][0]=="am" or a[0][0]=="are") and (a[1][1]=="PRP" or a[1][1]=="DT" or a[1][1]=="NN"or a[1][1]=="NNS" or a[1][1]=="NNP" or a[1][1]=="NNPS" or a[1][1]=="PRP$" ) and (a[-1][0]=="?") and (a[2][0]!="?"):
        return "一般疑问句"
   elif (a[0][0]=="is" or a[0][0]=="am" or a[0][0]=="are") and (a[1][1]=="PRP") and (a[-1][0]=="?"):
        return "反义疑问句"
   else:
        return "未知句型"

def zh_whattype(s0):
   kending=['是','肯定','确实','可以']
   fouding=['不','没有','非']
   baziju=['把']
   beiziju=['被']
   yiwen=['吗']
   for k in kending:
      if k in s0:
         return "肯定句"
   for f in fouding:
      if f in s0:
         return "否定句"
   for b in baziju:
      if b in s0:
         return "把字句"
   for bei in beiziju:
      if bei in s0:
         return "被字句"
   for y in yiwen:
      if y in s0:
         return "疑问句"
   return "未知句型"

def en_cixing(list3):#判断英文词性
   types=[]
   for s in list3:
      lower=s.lower() #将所有字母小写
      divided = nltk.word_tokenize(lower)#分词
      english_punctuations = [',','"','``',':',';', '(', ')', '[', ']', '&', '*', '@', '#', '$', '%']
      divided2 = [word for word in divided if word not in english_punctuations]
      #print(divided)
      tagged=nltk.pos_tag(divided2)#词性标注
      t=en_whattype(tagged)#判断句型
      #print(t)
      types.append(t)
   return types


def zh_cixing(list3):#判断中文词性
   types=[]
   for s in list3:
      #chinese_punctuations = ['<','>','《','》','”','“','：','；', '（', '）', '【', '】', '&', '*', '@', '#', '$', '%']
      #list4 = [word for word in s if word not in chinese_punctuations]
      #divided=SnowNLP("".join(list4)) #分词后的列表
      #tags=[x for x in divided.tags] #词性标注
      #判断句型
      #print(tags)
      t=zh_whattype(s)
      types.append(t)
   return types

def cunru(name,list1,list2): #存入csv文件
   dataframe = pd.DataFrame({'句子':list1,'句型':list2})
   dataframe.to_csv(name+".csv",index=False,sep=',',encoding="utf_8_sig")

if __name__=='__main__':
   en_filename="E:\Audrey\大三上\python\新建文件夹\His_dark_meterials_full_en\Pullman, Philip - His Dark Materials, Book 1.txt"
   zh_filename="E:\Audrey\大三上\python\新建文件夹\The_three_body_problem_full\《地球往事三部曲》全集.txt"
   
   en_file=duqu(en_filename)
   zh_file=duqu(zh_filename) 
   
   en_sentence=en_chouqu(en_file)#抽取英文句子
   zh_sentence=zh_chouqu(zh_file)#抽取中文句子
   
   en_type=en_cixing(en_sentence)#标注词性
   zh_type=zh_cixing(zh_sentence)
   
   #cunru("en",en_sentence,en_type)#存入csv文件
   #cunru("zh",zh_sentence,zh_type)

   with ProcessPoolExecutor(2) as pool:
      p = pool.map(cunru,[("en",en_sentence,en_type),("zh",zh_sentence,zh_type)])

   