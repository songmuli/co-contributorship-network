# #从本地读图文件
import pandas as pd
import numpy as np
import csv
import networkx as nx
#
nodeID=[]
int_nodeID=[]
authorID=[]
communityID=[]
file=open('D:/software/pycharm/xml/network2-id-label-community.csv','r')
datasets=csv.reader(file)
for data in datasets:
    nodeID.append(data[0])
    authorID.append(data[1])
    communityID.append(data[2])
for i in nodeID:
    int_nodeID.append(int(i))
print(int_nodeID)
dict1=dict(zip(int_nodeID,authorID))
dict2=dict(zip(int_nodeID,communityID))
print(dict1)
print(dict2)

nodeID=[]   #存放社区的节点ID（string）
labels=[]   #存放社区节点的标签
file=open('D:/software/pycharm/xml/network2-id-label-community.csv','r')
datasets=csv.reader(file)
for data in datasets:
  if data[2]=='56':
      nodeID.append(data[0])
      labels.append(data[1])
nodesID=[]   #int类型的节点ID
for n in nodeID:
    nodesID.append(int(n))
print(len(nodesID))
print('已获取要还原的社区网络的节点及其标签....')
dic=dict(zip(nodesID,labels))
print(dic)
# # #
# df=pd.read_csv('D:/software/pycharm/xml/venv/network1_medicine_df.csv')
# list1=df.values.tolist()
# edges_all=[tuple(i) for i in list1]
# print('已获取原最大联通子图的所有边....')
#
# edges = []
# for i in nodesID:
#     for j in edges_all:
#         if (j[0]==i) or (j[1]==i):
#             edges.append((j[0],j[1]))
# print(edges)
# print('已获取要还原的社区网络的边集合....')
#
# for e in range(len(edges)):
#     f=open('D:/software/pycharm/xml/network-community/n2-56/edges.csv','a',newline='')
#     writer = csv.writer(f)
#     writer.writerow(edges[e])
#     f.close()
# print('已将要还原的社区网络边集合写入本地....')


csv_file = 'D:/software/pycharm/xml/network-community/n2-56/edges.csv'
edges = pd.read_csv(csv_file)
print('读取数据完毕....')

print('开始构图....')
G = nx.from_pandas_edgelist(edges,source='source', target='target')
print(G.number_of_nodes())
print(G.number_of_edges())
print(G.nodes(data=True))

remove_node=[]
for node in G.nodes():
    if (node not in nodesID):
        remove_node.append(node)
G.remove_nodes_from(remove_node)  #去掉不是本社区的节点
print(G.number_of_nodes())
print(G.number_of_edges())

for node in G.nodes():
    for k1, v1 in dict1.items():
        if k1 == node:
            G.node[node]['label'] = v1
    for k2, v2 in dict2.items():
        if k2 == node:
            G.node[node]['community'] = v2
print(G.nodes(data=True))

nx.write_gexf(G,'network2-community56.gexf')








