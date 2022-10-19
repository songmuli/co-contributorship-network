# import csv
# import pymysql
#
# authorID=[]
# file=open('D:/software/pycharm/xml/network1-id-label-community.csv','r')
# datasets=csv.reader(file)
# for data in datasets:
#   if data[2]=='52':
#     authorID.append(data[1])
# print(len(authorID))
# print('已获得network1-community52的authorID....')
#
# #连接数据库
# db = pymysql.connect(host='localhost', user='root', password='123456', db='bishe')
# print("数据库连接成功！")
# cursor = db.cursor()
#
# paperID= [] #存放社区1的paperID
# for i in authorID:
#     cursor.execute('SELECT DISTINCT PaperID FROM contrib_pid_aid_medicine WHERE AuthorID=%s', i)
#     results_pid=cursor.fetchall()
#     for res_pid in results_pid:
#         paperID.append(res_pid[0])
# print(len(paperID))
# PaperID=[]
# for p in paperID:
#     if p not  in PaperID:
#         PaperID.append(p)
# print(len(PaperID))
# print('已获得network2-community20的paperID....')
#
# doi=[] #存放社区1的文章doi
# for pid in PaperID:
#     cursor.execute('SELECT DISTINCT doi FROM contrib_pid_aid_medicine WHERE PaperID=%s', pid)
#     results_doi = cursor.fetchall()
#     for res_doi in results_doi:
#         doi.append(res_doi[0])
# print(len(doi))
# print('已获得network2-community20的文章doi....')
# #
# title=[]
# abstract=[]
# for d in doi:
#     cursor.execute('SELECT article_name,abstract FROM metadata WHERE doi=%s', d)
#     results = cursor.fetchall()
#     for res in results:
#         title.append(res[0])
#         abstract.append((res[1]))
# print(len(title))
# print(len(abstract))
# print('已获得network2-community20的文章title和abstract....')
# # # # # # #
# for t in range(5):
#     file1_name=str(t+1)+'.txt'
#     f1=open('D:/software/pycharm/xml/n2-20/title/'+file1_name,'w',encoding='utf-8')
#     f1.write(title[t])
#     f1.close()
# print('已将network2-community20的文章title写入txt....')
#
# for k in range(6):
#     file_name=str(k+1)+'.txt'
#     f=open('D:/software/pycharm/xml/n2-20/title+abstract/'+file_name,'w',encoding='utf-8')
#     f.write(title[k]+'\n')
#     f.write(abstract[k])
#     f.close()
# print('已将network2-community20的文章title+abstract写入txt....')
# # # #
# # # # for a in range(21):
# # # #     file2_name=str(a+1)+'.txt'
# # # #     f2=open('D:/software/pycharm/xml/network2-community4/abstract/'+file2_name,'w',encoding='utf-8')
# # # #     f2.write(abstract[a])
# # # #     f2.close()
# # # # print('已将network2-community4的文章abstract写入txt....')
# # # #

# # # # # # #


# #
# # #
# # #
# #
# keybert算法提取每篇文章关键字并写入txt
from keybert import KeyBERT
import pandas as pd
import csv

stop_words=['of','in','is','were','with','for','into','the','to','and','on','in','we','at','that','from','among','during']
all_articles_keywords = []
for i in range(5):
    file1_name=str(i+1)+'.txt'
    with open('D:/software/pycharm/xml/n2-55/title+abstract/'+file1_name,'r', encoding='utf-8') as f:
        data=f.read()
    kw_model = KeyBERT()
    keywords=kw_model.extract_keywords(data, keyphrase_ngram_range=(1, 2), stop_words=stop_words, top_n=1)
    all_articles_keywords += keywords
# data=pd.DataFrame(all_articles_keywords,columns=['keyword','probability'])
# data.to_csv('D:/software/pycharm/xml/network1-community30/title+abstract/all_articles_keywords.csv',sep='\t',index=0,header=0)
# print('已获得各篇文章的关键词.....')
import openpyxl
wb = openpyxl.Workbook()
ws = wb.create_sheet('n2-55', index=0)
ws["A1"] = "keywords"
ws["B1"] = "probability"
n=2
for i in all_articles_keywords:
    ws.cell(row=n, column=1, value=i[0])
    ws.cell(row=n, column=2, value=i[1])
    n += 1
wb.save('D:/software/pycharm/xml/n2-55/title+abstract/all_titles_keywords-k2.xlsx')
# # #
#
#
#
#
#
# #
# #
