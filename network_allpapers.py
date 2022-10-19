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


# cursor.execute("select * from contrib;")


# tree = ET.parse('D:/2022bishe/pbio/file@id=10.1371%2Fjournal.pbio.1002611&type=manuscript')
# root = tree.getroot()

  G = nx.Graph()

  new_contrib_authors = []
  for con in contrib_type:
   # sql_chongfu_contrib = "SELECT author_name FROM contrib where (doi = %s) & (contrib_type = %s)"
   cursor.execute()
   contrib_authors = []
   com_list = []
   result_authors = cursor.fetchall()
   # print(result_authors)
   for res_authors in result_authors:
       contrib_authors.append(res_authors[0])
   if len(contrib_authors) != 1:
       com_list = list(combinations(contrib_authors, 2))
       new_contrib_authors += com_list
       # G.add_edges_from(com_list)
   else:
       for aut in contrib_authors:
           com_list = [(aut, aut)]
           new_contrib_authors += com_list
       # G.add_edges_from(com_list)
  contrib_weight = []
  for new_res_author in new_contrib_authors:
    weight = new_contrib_authors.count(new_res_author)
    contrib_weight.append(weight)
  new_contrib_author_weight = list(zip(new_contrib_authors,contrib_weight))

  for i, j in new_contrib_author_weight:
    G.add_edge(i[0], i[1], weight=j)

  pos = nx.spring_layout(G)
  nx.draw(G, pos, with_labels=True)
  lables = nx.get_edge_attributes(G, 'weight')
  nx.draw_networkx_edge_labels(G, pos, lables, label_pos=0.5)
  plt.axis('on')
  plt.xticks([])
  plt.yticks([])
  plt.savefig("D:/2022bishe/total/network/Graph-%s.png"%(doi), format="PNG")
  plt.show()
  plt.close()

  # print(G.edges(data=True))
# print(G.get_edge_data('Warnhoff Kurt', 'Warnhoff Kurt'))
# nx.write_gexf(G, 'pbio_2000080.gexf')
# print(G.number_of_nodes())
# print(G.number_of_edges())
# print(G.degree)