import json
import csv
import pandas as pd
n_dic = {}   #存放int键的字典
labels = [] #存放每个节点的社区号
with open("D:/2022bishe/github/GEMSEC-master/output/assignments/network2_medicine_31_128d.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
for key, value in load_dict.items():  #原字典的的键是string类型，为得到有序的节点社区号，需转换为int类型
    n_key = int(key)
    n_value = value
    n_dic[n_key] = n_value
print(n_dic)
for v in n_dic.values():
    labels.append(v)
print(labels)
name=['communityID']
communityID=pd.DataFrame(columns=name,data=labels)
print(communityID)
communityID.to_csv('network2_community_31.csv',index=False)




#
#
# nodes_n=[]
# edges_n=[]
# for c in nx.connected_components(G):
#
#     nodes_number=G.subgraph(c).number_of_nodes()
#     nodes_n.append(nodes_number)
#     edges_number=G.subgraph(c).number_of_edges()
#     edges_n.append(edges_number)
#
# print(nodes_n)
# print(edges_n)
#
# result_dic={}
# for i in nodes_n:
#     if i not in result_dic:
#         result_dic[i]=1
#     else:
#         result_dic[i]+=1
# print(result_dic)
# x=[]
# y=[]
# xt=range(1,100,10)
# yt=range(1,800,79)
# for k,v in result_dic.items():
#   if k!=9233:
#     x.append(k)
#     y.append(v)
# print(min(x),max(x))
# print(min(y),max(y))
# plt.figure(figsize=(10,5))
# plt.bar(x,y,color = 'blue',width = 2)
#
# plt.xticks(xt)
# plt.yticks(yt)
# plt.show()



    # if nodes_number > 50:
    #   i+=1
    #   print('第%d个子图：节点数为%d, 边数为%d'  %(i, nodes_number, edges_number))


# # 从本地读图文件
# import pandas as pd
# import numpy as np
# import csv
# import networkx as nx
# import matplotlib.pyplot as plt
#
# csv_file = 'D:/2022bishe/github/GEMSEC-master/data/network1_medicine_df.csv'
# edges = pd.read_csv(csv_file)
# print('读取数据完毕....')
# # print(edges)
# print('开始构图....')
# G = nx.from_pandas_edgelist(edges,source='source', target='target')
# print(G.number_of_nodes())
# print(G.number_of_edges())
# # 分别得到nodeid,authorid,communityid
# import csv
# nodeID=[]
# authorID=[]
# communityID=[]
# file=open('D:/software/pycharm/xml/network1_nodeslabel.csv','r')
# datasets=csv.reader(file)
# for data in datasets:
#     nodeID.append(data[0])
#     authorID.append(data[1])
#     communityID.append(data[2])
#
# for i in range(9501):
#     G.node[i]['label']=authorID[i]
#     G.node[i]['communityID']=communityID[i]
# print(G.nodes(data=True))
# nx.write_gexf(G,'network1_medicine_newG.gexf') #划分好社区的图




