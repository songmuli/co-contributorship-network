import pandas as pd
import numpy as np
import csv
import networkx as nx
import matplotlib.pyplot as plt

#原图
csv_file = 'D:/2022bishe/github/GEMSEC-master/data/network2_medicine_df.csv'
edges = pd.read_csv(csv_file)
print('读取数据完毕....')
# print(edges)
print('开始构图....')
G = nx.from_pandas_edgelist(edges,source='source', target='target')

#最大联通子图
largest=max(nx.connected_components(G),key=len)
new_G = G.subgraph(largest)
print(new_G.number_of_nodes())
print(new_G.number_of_edges())

# 将new_G的edgelist存储于csv文件
# df = nx.to_pandas_edgelist(new_G)
# print(df)
# df.to_csv('D:/2022bishe/github/GEMSEC-master/data/network2_medicine_df.csv', sep=',', index=False)