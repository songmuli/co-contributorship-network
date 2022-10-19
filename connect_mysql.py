import pymysql
from itertools import combinations
import numpy as np
db = pymysql.connect(host='localhost', user='root', password='123456', db='bishe')
print("数据库连接成功！")
cursor = db.cursor()
sql1 = "SELECT DISTINCT contribution_type FROM contrib WHERE doi = '10.1371/journal.pbio.2000245';"
cursor.execute(sql1)
contrib_type = []
result_contrib = cursor.fetchall()
for res in result_contrib:
     contrib_type.append(res[0])
# print(contrib_type)

Doi = '10.1371/journal.pbio.2000245'
new_contrib_authors = []
for con in contrib_type:
   # sql_chongfu_contrib = "SELECT author_name FROM contrib where (doi = %s) & (contrib_type = %s)"
   cursor.execute('SELECT author_name FROM contrib where (doi = %s) & (contribution_type = %s)', (Doi, con))
   contrib_authors = []
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
# print(new_contrib_authors)

contrib_weight = []
for new_res_author in new_contrib_authors:
    weight = new_contrib_authors.count(new_res_author)
    contrib_weight.append(weight)
new_contrib_author_weight = list(zip(new_contrib_authors,contrib_weight))
print(new_contrib_author_weight)
for i, j in new_contrib_author_weight:
    print(i[0], i[1], j)



