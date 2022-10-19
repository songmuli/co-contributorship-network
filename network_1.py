import networkx as nx
import pymysql
from itertools import combinations
import pandas as pd


#连接数据库
db = pymysql.connect(host='localhost', user='root', password='123456', db='bishe')
print("数据库连接成功！")
cursor = db.cursor()

#获取所有的论文
sql_pid = 'SELECT DISTINCT PaperID FROM contrib_pid_aid_medicine'
cursor.execute(sql_pid)
papers_pid = []
results_pid = cursor.fetchall()
for res_pid in results_pid:
    papers_pid.append(res_pid[0])
print('成功获取所有论文id....')

#获取所有的作者（节点）
authors_aid_one = []  #存放所有作者节点
sql_aid = 'SELECT DISTINCT AuthorID FROM contrib_pid_aid_medicine'
cursor.execute(sql_aid)
results_author = cursor.fetchall()
for res_au in results_author:
   authors_aid_one.append(res_au[0])
print('成功获取所有节点....')

# print(len(authors_aid_one))

#获取作者数>1论文的合著关系（边）
authors_aid_two = []  #如果一篇文章作者数>1，将该文章作者组合后，加入此列表。两两作者之间形成边。
for paper_pid in papers_pid:
    # print(paper_pid)
    perpaper_aid = []  #每篇文章的作者集合
    perpaper_com = []  #每篇文章组合后的作者集合
    cursor.execute('SELECT DISTINCT AuthorID FROM contrib_pid_aid_medicine WHERE PaperID=%s', paper_pid)
    results_aid = cursor.fetchall()
    for res_aid in results_aid:
        perpaper_aid.append(res_aid[0])
    if len(perpaper_aid) > 1:
        perpaper_com = list(combinations(perpaper_aid, 2))
    authors_aid_two += perpaper_com
print('成功获取所有边.....')

#获得边的权值
# collab_weight = []  #合作的次数（组合出现的次数）即为边的权重
# for new_res_author in authors_aid_two:
#   weight = authors_aid_two.count(new_res_author)
#   collab_weight.append(weight)
# new_collab_author_weight = list(zip(authors_aid_two, collab_weight)) #存放边及其权重[('node1','node2'),weight]
#
# authors_two_weight = [] #边＋权重（'node1','node2',weight）
# for i, j in new_collab_author_weight:
#     tuple = (i[0], i[1], j)
#     authors_two_weight.append(tuple)
# print(authors_two_weight)

#开始画图
G = nx.Graph()
G.add_nodes_from(authors_aid_one)
G.add_edges_from(authors_aid_two)
print(G.number_of_nodes())
print(G.number_of_edges())
# nx.write_gexf(G,'your_file_name.gexf')

# #移除孤立节点
# G.remove_nodes_from(list(nx.isolates(G)))
# print(G.number_of_nodes())
#
# #找出最大联通子图
# largest=max(nx.connected_components(G),key=len)
# largest_G = G.subgraph(largest)
# print(largest_G.number_of_nodes())
# print(largest_G.number_of_edges())
#
#
# #lables与id互换，以id索引
# nodes = []
# edges = []
# nodes_id = dict()
# nodes_label = dict()
# for id, label in enumerate(largest_G.nodes()):
#     nodes_id[label] = id
#     nodes_label[id] = label
#     nodes.append(id)
# for (u, v) in largest_G.edges():
#     edges.append((nodes_id[u], nodes_id[v]))
# new_G = nx.Graph()
# new_G.add_nodes_from(nodes)
# for node in nodes:
#     new_G.add_node(node, labels = node)
# new_G.add_edges_from(edges)
#
# # print(nodes_label)
# with open('nodeslabel.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in nodes_label.items()]
# print('成功写入nodeslabel.csv')
#
#
#
#
# # 将G的edgelist存储于csv文件
# df = nx.to_pandas_edgelist(new_G)
# print(df)
# df.to_csv('D:/2022bishe/github/GEMSEC-master/data/network1_medicine_df.csv', sep=',', index=False)










