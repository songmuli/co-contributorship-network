#从本地读图文件
import pandas as pd
import numpy as np
import csv
import networkx as nx
import matplotlib.pyplot as plt

csv_file = 'D:/2022bishe/github/GEMSEC-master/data/network2_medicine_df.csv'
edges = pd.read_csv(csv_file)
print('读取数据完毕....')
# print(edges)
print('开始构图....')
G = nx.from_pandas_edgelist(edges,source='source', target='target')
print(G.number_of_nodes())
print(G.number_of_edges())

print('开始获取节点的标签列表....')
node_label=[]  #按序存放每个节点的标签
file=open('D:/software/pycharm/xml/network2_nodeslabel.csv','r')
datasets=csv.reader(file)
for data in datasets:
    node_label.append(data[1])
print(G.nodes(data=True))

print('开始为每个节点添加标签')
for i in range(9233):
    G.node[i]['label'] = node_label[i]


print(G.nodes(data=True))
print(nx.degree(G))
result=dict(nx.degree(G))
key=list(result.keys())
value=list(result.values())
result_excel=pd.DataFrame()
result_excel['节点ID']=key
result_excel['degree']=value
result_excel.to_excel('D:/software/pycharm/xml/network2_nodes_degree.xlsx')
# nx.write_gexf(G,'network2_maxG.gexf')