import networkx as nx
import pymysql
from itertools import combinations


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
print('获取paperID完毕...')

#获取所有的作者（节点）
authors_aid_one = []  #存放所有作者节点['node1','node2',.........]
sql_aid = 'SELECT DISTINCT AuthorID FROM contrib_pid_aid_medicine'
cursor.execute(sql_aid)
results_author = cursor.fetchall()
for res_au in results_author:
   authors_aid_one.append(res_au[0])
print('获取AuthorID完毕....')


#获取所有文章的贡献合作关系（边）
new_contrib_authors = []  #合作完成同一贡献的作者之间连线（边集合）
for paper_pid in papers_pid:
    cursor.execute("SELECT DISTINCT contribution_type FROM contrib_pid_aid_medicine WHERE PaperID = %s", paper_pid)
    contrib_type = [] #每篇文章的贡献类型
    result = cursor.fetchall()
    for res in result:
        contrib_type.append(res[0])
    for con in contrib_type:
        contrib_authors = [] #存放每个贡献类型下的所有作者
        com_list = []    #将合作完成同一贡献的作者们两两组合
        cursor.execute("SELECT DISTINCT AuthorID FROM contrib_pid_aid_medicine WHERE (PaperID = %s) and (contribution_type = %s)", (paper_pid, con))
        result_authors = cursor.fetchall()
        # print(result_authors)
        for res_authors in result_authors:
            contrib_authors.append(res_authors[0])
        if len(contrib_authors) != 1:
            com_list = list(combinations(contrib_authors, 2))
            new_contrib_authors += com_list
        else:
            for aut in contrib_authors:
                com_list = [(aut, aut)]
                new_contrib_authors += com_list
# contrib_weight = []  #合作的次数（组合出现的次数）即为边的权重
# for new_res_author in new_contrib_authors:
#   weight = new_contrib_authors.count(new_res_author)
#   contrib_weight.append(weight)
# new_contrib_author_weight = list(zip(new_contrib_authors, contrib_weight)) #存放边及其权重[('node1','node2'),weight]
# print('获得初始边+权重完毕...')
#
#
# authors_two_weight = [] #边＋权重（'node1','node2',weight）
# for i, j in new_contrib_author_weight:
#     tuple = (i[0], i[1], j)
#     authors_two_weight.append(tuple)
# print('获得元组列表型边+权重完毕....')


#开始画图
G = nx.Graph()
G.add_nodes_from(authors_aid_one)
G.add_edges_from(new_contrib_authors)
print(G.number_of_nodes())
print(G.number_of_edges())


# nx.write_gexf(G,'network2_medicine.gexf')

# G.remove_nodes_from(list(nx.isolates(G)))
# print(G.number_of_nodes())
#
# #找出最大联通子图
# largest=max(nx.connected_components(G),key=len)
# largest_G = G.subgraph(largest)
# print(largest_G.number_of_nodes())
# print(largest_G.number_of_edges())
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
# print('节点id与label互换完毕....')
# #
# #
# # with open('network2_nodesid.csv', 'w') as f:
# #     [f.write('{0},{1}\n'.format(key, value)) for key, value in nodes_id.items()]
# # print('成功写入nodesid.csv')
# #
# with open('network2_nodeslabel.csv', 'w') as f:
#     [f.write('{0},{1}\n'.format(key, value)) for key, value in nodes_label.items()]
# print('成功写入nodeslabel.csv')
#
# df = nx.to_pandas_edgelist(new_G)
# print(df)
# df.to_csv('D:/2022bishe/github/GEMSEC-master/data/network2_medicine_df.csv', sep=',', index=False)