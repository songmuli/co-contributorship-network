import pandas as pd
import numpy as np
import csv
import networkx as nx
#
nodeID_11=[]   #存放社区的节点ID（string）
nodeID_12=[]   #存放社区的节点ID（string）
file=open('D:/software/pycharm/xml/network2-id-label-community.csv','r')
datasets=csv.reader(file)
for data in datasets:
  if data[2]=='50':
      nodeID_11.append(data[0])
  if data[2]=='51':
      nodeID_12.append(data[0])
nodesID_11=[]   #int类型的节点ID
for n in nodeID_11:
    nodesID_11.append(int(n))
print(len(nodesID_11))
nodesID_12=[]   #int类型的节点ID
for n in nodeID_12:
    nodesID_12.append(int(n))
print(len(nodesID_12))


df=pd.read_csv('D:/software/pycharm/xml/venv/network2_medicine_df.csv')
list1=df.values.tolist()
edges_all=[tuple(i) for i in list1]
print('已获取原最大联通子图的所有边....')

edges = []
for i in nodesID_11:
    for j in edges_all:
        if (j[0]==i) or (j[1]==i):
            edges.append((j[0],j[1]))
print(edges)
print('已获取要还原的社区网络的边集合....')

count=0
for i in nodesID_12:
    for j in edges:
        if (j[0]==i) or (j[1]==i):
            count += 1
print(count)

