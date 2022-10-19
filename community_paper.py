import json
n_dic = {}   #存放int键的字典
with open("D:/2022bishe/github/GEMSEC-master/output/assignments/network1_medicine_20.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
for key, value in load_dict.items():  #原字典的的键是string类型，为得到有序的节点社区号，需转换为int类型
    n_key = int(key)
    n_value = value
    n_dic[n_key] = n_value
print(n_dic)

community0=[] #属于社区0的所有节点
community1=[]
community2=[]
community3=[]
community4=[]
community5=[]
community6=[]
community7=[]
community8=[]
community9=[]
community10=[]
community11=[]
community12=[]
community13=[]
community14=[]
community15=[]
community16=[]
community17=[]
community18=[]
community19=[]

for k, v in n_dic.items():
    if v==0:
        community0.append(k)
    if v==1:
        community1.append(k)
    if v==2:
        community2.append(k)
    if v==3:
        community3.append(k)
    if v==4:
        community4.append(k)
    if v==5:
        community5.append(k)
    if v==6:
        community6.append(k)
    if v==7:
        community7.append(k)
    if v==8:
        community8.append(k)
    if v==9:
        community9.append(k)
    if v==10:
        community10.append(k)
    if v==11:
        community11.append(k)
    if v==12:
        community12.append(k)
    if v==13:
        community13.append(k)
    if v==14:
        community14.append(k)
    if v==15:
        community15.append(k)
    if v==16:
        community16.append(k)
    if v==17:
        community17.append(k)
    if v==18:
        community18.append(k)
    if v==19:
        community19.append(k)
print('成功得到每个社区的所有节点ID')

import csv
csvFive = open('network1_nodeslabel.csv','r')
reader = csv.reader(csvFive)
result = {} #存放"节点ID--作者ID"的字典
for item in reader:
   result[int(item[0])]=item[1]
csvFive.close()
print('成功获取“节点id--作者id”')

# print('开始匹配社区19的作者ID.....')
# community19_aid = []
# for i in community19:
#     for k, v in result.items():
#         if k==i:
#             community19_aid.append(v)
# print(len(community19_aid))
print('--------------')


import pymysql
#连接数据库
db = pymysql.connect(host='localhost', user='root', password='123456', db='bishe')
print("数据库连接成功！")
cursor = db.cursor()

# print('正在匹配社区19的doi.....')
# community19_pid = []
# for d in community19_aid:
#     cursor.execute('SELECT DISTINCT doi FROM contrib_pid_aid_medicine WHERE AuthorID=%s', d)
#     results = cursor.fetchall()
#     for res in results:
#         community19_pid.append(res[0])
# f=open('community19_doi.txt', 'w')
# for i in community19_pid:
#    f.write(i+'\n')

#

print('-----------------------')
print('从数据库中读取community19的doi')
community19_doi = []
cursor.execute('SELECT DISTINCT doi FROM community19_doi')
results = cursor.fetchall()
for res in results:
  community19_doi.append(res[0])
print(len(community19_doi))


print('-----------------------')
print('正在匹配社区19的文章标题和摘要.....')
community19_title = []   #存放社区0的文章标题
community19_abstract = []  #存放社区0的文章摘要
# community1_article = {}   #存放社区0的文章信息（标题：摘要）
for p in community19_doi:
    cursor.execute('SELECT article_name,abstract FROM metadata_hascontrib WHERE doi=%s', p)
    results = cursor.fetchall()
    for res in results:
        community19_title.append(res[0])
        community19_abstract.append(res[1])
# community1_article = dict(zip(community1_title,community1_abstract))
#
#
f1 = open('community19_titile.txt','w',encoding='utf-8')
for t in community19_title:
    f1.write(t+'\n')
print('成功将文章标题写入txt')
print(len(community19_title))


f2 = open('community19_abstract.txt', 'w',encoding='utf-8')
for a in community19_abstract:
    f2.write(a+'\n')
print('成功将文章摘要写入txt')
print(len(community19_abstract))

