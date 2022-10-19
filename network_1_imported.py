import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pymysql
from itertools import combinations

def get_network1():
  #连接数据库
  db = pymysql.connect(host='localhost', user='root', password='123456', db='bishe')
  print("数据库连接成功！")
  cursor = db.cursor()

  #获取所有的论文
  sql_pid = 'SELECT DISTINCT PaperID FROM contrib_pid_aid_bio'
  cursor.execute(sql_pid)
  papers_pid = []
  results_pid = cursor.fetchall()
  for res_pid in results_pid:
      papers_pid.append(res_pid[0])

  #获取所有的作者（节点）
  authors_aid_one = []  #存放所有作者节点
  sql_aid = 'SELECT DISTINCT AuthorID FROM contrib_pid_aid_bio'
  cursor.execute(sql_aid)
  results_author = cursor.fetchall()
  for res_au in results_author:
     authors_aid_one.append(res_au[0])
  # print(len(authors_aid_one))

  #获取作者数>1论文的合著关系（边）
  authors_aid_two = []  #如果一篇文章作者数>1，将该文章作者组合后，加入此列表。两两作者之间形成边。
  for paper_pid in papers_pid:
    # print(paper_pid)
    perpaper_aid = []  #每篇文章的作者集合
    perpaper_com = []  #每篇文章组合后的作者集合
    cursor.execute('SELECT DISTINCT AuthorID FROM contrib_pid_aid_bio WHERE PaperID=%s', paper_pid)
    results_aid = cursor.fetchall()
    for res_aid in results_aid:
        perpaper_aid.append(res_aid[0])
    if len(perpaper_aid) > 1:
        perpaper_com = list(combinations(perpaper_aid, 2))
    authors_aid_two += perpaper_com

  #获得边的权值
  collab_weight = []  #合作的次数（组合出现的次数）即为边的权重
  for new_res_author in authors_aid_two:
    weight = authors_aid_two.count(new_res_author)
    collab_weight.append(weight)
  new_collab_author_weight = list(zip(authors_aid_two, collab_weight)) #存放边及其权重[('node1','node2'),weight]

  authors_two_weight = [] #边＋权重（'node1','node2',weight）
  for i, j in new_collab_author_weight:
      tuple = (i[0], i[1], j)
      authors_two_weight.append(tuple)
  # print(authors_two_weight)

  #开始画图
  G = nx.Graph()
  pos = nx.spring_layout(G, k=0.15)
  G.add_nodes_from(authors_aid_one)
  G.add_weighted_edges_from(authors_two_weight)

  return  G

#infomap
# from infomap import Infomap
# im = Infomap(silent=True)
# mapping = im.add_networkx_graph(G)







# #node2vec
# n2v = Node2Vec(G, dimensions=128, walk_length=10, num_walks=20, workers=1)
# model = n2v.fit(window=10, min_count=1)
# node_embeddings = model.wv.vectors
# print(node_embeddings)
#
# #tsne
# from sklearn.manifold import TSNE
# tsne = TSNE(n_components=2)
# node_embeddings_2d = tsne.fit_transform(node_embeddings)
# print(node_embeddings_2d)

