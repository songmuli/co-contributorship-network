from xml.dom.minidom import parse
from prettytable import PrettyTable
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("D:/2022bishe/failed_journal/file@id=10.1371%2Fjournal.pone.0158988&type=manuscript")
root = DOMTree.documentElement

# #出版商
journals = root.getElementsByTagName("journal-title")
journal = journals[0].firstChild.data
# print("出版商：", journal)

#文章名
articles = root.getElementsByTagName("article-title")
article = articles[0].firstChild.data
# print("文章名称：", article)

#日期
dates = root.getElementsByTagName("pub-date")
pub_dates = dates[1]
# month = pub_dates.getElementsByTagName('month')[0].firstChild.data
year = pub_dates.getElementsByTagName('year')[0].firstChild.data
# date = year
# print("出版年份: ", year)

#作者名
names = root.getElementsByTagName("contrib")
names_list = []
for name in names:
  if "author" == name.getAttribute("contrib-type"):
    surname = name.getElementsByTagName('surname')[0].childNodes[0].nodeValue
    given_name = name.getElementsByTagName('given-names')[0].childNodes[0].nodeValue
    author_name = given_name + '  ' + surname + '、 '
    names_list.append(author_name)
# print("作者姓名： ", end='')
authors_name = ''
for i in names_list:
 authors_name += i
# print(authors_name)
# print('\n')
#
#贡献数据
author_notes = root.getElementsByTagName("fn")
author_note = author_notes[1]
# print(author_note)
contrib = author_note.getElementsByTagName('p')[0].firstChild.data
# print("作者贡献：\n", contrib)

#以表格形式输出
tb = PrettyTable()
tb.field_names = ["期刊", "文章名称", "出版日期", "作者", "贡献数据"]
tb.add_row([journal, article, year, authors_name, contrib])
print(tb)

# information = journal + '  ————  ' + article + '  ————  ' + date + '  ————  ' + authors_name + '  ————  ' + contrib
# #结果写入txt
# with open("test.txt", "w", encoding='utf-8') as f:
#   f.write(information)