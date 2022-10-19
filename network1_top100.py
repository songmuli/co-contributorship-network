import csv
authorID_top100=[]
file1=open('D:/2022bishe/github/result.csv','r')
datasets1=csv.reader(file1)
for data in datasets1:
    if len(authorID_top100)<149:
        authorID_top100.append(data[0])
print(authorID_top100)
print('已获取被引前100的作者ID....')

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
dict1=dict(zip(authorID,int_nodeID))
dict2=dict(zip(authorID,communityID))
print(dict1)
print(dict2)

nodeID_top100=[]
communityID_top100=[]
for i in authorID_top100:
    for k1,v1 in dict1.items():
        if k1==i:
            nodeID_top100.append(v1)
    for k2,v2 in dict2.items():
        if k2==i:
            communityID_top100.append(v2)
dict1_top100=dict(zip(nodeID_top100,authorID_top100))
dict2_top100=dict(zip(nodeID_top100,communityID_top100))
print(len(dict1_top100))
print(len(dict2_top100))
print('已获取被引前200的节点信息....')


# #
# import pandas as pd
# df=pd.read_csv('D:/software/pycharm/xml/venv/network2_medicine_df.csv')
# list1=df.values.tolist()
# edges_all=[tuple(i) for i in list1]
# print('已获取原最大联通子图的所有边....')
# #
# edges = []
# for i in nodeID_top100:
#     for j in edges_all:
#         if (j[0]==i) or (j[1]==i):
#             edges.append((j[0],j[1]))
# print(edges)
# print('已获取要还原的社区网络的边集合....')
# #
# for e in range(len(edges)):
#     f=open('D:/software/pycharm/xml/network2_top100_edges.csv','a',newline='')
#     writer = csv.writer(f)
#     writer.writerow(edges[e])
#     f.close()
# print('已将要还原的网络边集合写入本地....')

import pandas as pd
import networkx as nx

csv_file = 'D:/software/pycharm/xml/network2_top100_edges.csv'
edges = pd.read_csv(csv_file)
print('读取数据完毕....')

print('开始构图....')
G = nx.from_pandas_edgelist(edges,source='source', target='target')
print(G.number_of_nodes())
print(G.number_of_edges())
print(G.nodes(data=True))

remove_node=[]
for node in G.nodes():
    if (node not in nodeID_top100):
        remove_node.append(node)
G.remove_nodes_from(remove_node)

print(G.number_of_nodes())
print(G.number_of_edges())
for node in G.nodes():
    for k1,v1 in dict1_top100.items():
        if k1==node:
            G.node[node]['label']=v1
    for k2,v2 in dict2_top100.items():
        if k2==node:
            G.node[node]['community']=v2
print(G.nodes(data=True))
nx.write_gexf(G,'network2-top100.gexf')

