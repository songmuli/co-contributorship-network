import os
import os.path
from xml.dom.minidom import parse
from prettytable import PrettyTable
import xml.dom.minidom

# tb = PrettyTable()
# tb.field_names = ["期刊", "文章名称", "出版日期", "作者", "贡献数据"]
path = 'D:/2022bishe/pbio/'
files = os.listdir(path)
i = 0
j = 0
for xmlFile in files:
    # print(xmlFile)
  DOMTree = xml.dom.minidom.parse(os.path.join(path,xmlFile))
  root = DOMTree.documentElement

#出版商
#   journals = root.getElementsByTagName("journal-title")
#   journal = journals[0].firstChild.data
#   i += 1
#   print("出版商：", journal)
# print(i)
  # print(xmlFile)

#
 #文章名
  # articles = root.getElementsByTagName("article-title")
  # article = articles[0].data
  # print("文章名称：", article)


#日期
  # dates = root.getElementsByTagName("pub-date")
  # pub_dates = dates[1]
  # year = pub_dates.getElementsByTagName('year')[0].firstChild.data
  # date = year + '年'
  # print("出版日期: ", date)
#
#doi
  # dois_list = []
  # dois = root.getElementsByTagName("article-id")
  # for doi in dois:
  #   if doi.getAttribute("pub-id-type") == "doi":
  #     article_doi = doi.firstChild.data
  #     dois_list.append(article_doi)
  # print(dois_list[0])
  # print(doi)

# #作者名
  names = root.getElementsByTagName("contrib")
  names_list = []
  corresp_list = []
  for name in names:
    try:
     if "author" == name.getAttribute("contrib-type"):
        surname = name.getElementsByTagName('surname')[0].childNodes[0].nodeValue
        given_name = name.getElementsByTagName('given-names')[0].childNodes[0].nodeValue
        author_name = given_name + '  ' + surname
        names_list.append(author_name)
        xrefs = name.getElementsByTagName("xref")
        for xref in xrefs:
          if xref.getAttribute("ref-type") == 'corresp':
            corresp_list.append(author_name)
    except IndexError:
        collab = name.getElementsByTagName('collab')[0].childNodes[0].nodeValue
        names_list.append(collab)
  # for nm in range(len(names_list)-1):
  #   print(names_list[nm]+' ， ', end='')
  # print(names_list[-1])
  # print(" ， ".join(str(nm) for nm in names_list))
  print(" , ".join(str(corresp) for corresp in corresp_list))
  print(xmlFile)

#   print('\n')
# #
# #贡献数据
#   author_notes = root.getElementsByTagName("fn")
#   author_note = author_notes[1]
# # print(author_note)
#   contrib = author_note.getElementsByTagName('p')[0].firstChild.data
#   print("作者贡献：\n", contrib)
#
# #以表格形式输出

# tb.add_row([journal, article, date, authors_name, contrib])
# print(tb)

#将结果输出到excel
