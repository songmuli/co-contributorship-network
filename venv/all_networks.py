import xml.etree.cElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import pymysql
from itertools import combinations
import os.path
import openpyxl


db = pymysql.connect(host='localhost', user='root', password='123456', db='bishe')
print("数据库连接成功！")
cursor = db.cursor()
cursor.execute('SELECT DISTINCT doi FROM contrib;')
result_doi = cursor.fetchall()
all_contrib_author = []  #所有文章的作者合作组合
for Doi in result_doi:
  str_doi = ''.join(Doi)
  doi1 = str_doi[16:20]
  doi2 = str_doi[-7:]
  doi = doi1 + doi2
  cursor.execute("SELECT DISTINCT contribution_type FROM contrib WHERE doi = %s", Doi)
  contrib_type = []
  result = cursor.fetchall()
  for res in result:
     contrib_type.append(res[0])

  G = nx.Graph()

  new_contrib_authors = [] #每篇文章的作者所有组合列表
  for con in contrib_type:
   # sql_chongfu_contrib = "SELECT author_name FROM contrib where (doi = %s) & (contrib_type = %s)"
   cursor.execute('SELECT author_name FROM contrib where (doi = %s) & (contribution_type = %s)', (Doi, con))
   contrib_authors = [] #每种贡献的作者集合
   com_list = []        #每种贡献组合后的作者集合
   result_authors = cursor.fetchall()
   # print(result_authors)
   for res_authors in result_authors:
       contrib_authors.append(res_authors[0])
   if len(contrib_authors) != 1: #如果作者数不等于1，就进行两两组合组合
       com_list = list(combinations(contrib_authors, 2))
       new_contrib_authors += com_list
       # G.add_edges_from(com_list)
   else:
       for aut in contrib_authors:
           com_list = [(aut, aut)]
           new_contrib_authors += com_list

       # G.add_edges_from(com_list)
  all_contrib_author.append(new_contrib_authors) #
contrib_weight = []  #每个作者组合出现的次数，即边的权重
for all_res_author in all_contrib_author:
  weight = all_contrib_author.count(all_res_author)
  contrib_weight.append(weight)
new_contrib_author_weight = list(zip(all_contrib_author,contrib_weight))
for i, j in new_contrib_author_weight:
   # G.add_edge(i[0], i[1], weight=j)
   print(i[0],i[1],j)

  # pos = nx.spring_layout(G)
  # nx.draw(G, pos, with_labels=True)
  # lables = nx.get_edge_attributes(G, 'weight')
  # nx.draw_networkx_edge_labels(G, pos, lables, label_pos=0.5)
  # plt.axis('on')
  # plt.xticks([])
  # plt.yticks([])
  # plt.savefig("D:/2022bishe/total/network/Graph-%s.png"%(doi), format="PNG")
  # plt.show()
  # plt.close()