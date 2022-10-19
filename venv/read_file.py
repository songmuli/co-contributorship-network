from xml.dom.minidom import parse
from prettytable import PrettyTable
import xml.dom.minidom
import os
import os.path

# DOMTree = xml.dom.minidom.parse("D:/2022bishe/xml/file@id=10.1371%2Fjournal.pbio.1002332&type=manuscript")
# root = DOMTree.documentElement
path = "D:/2022bishe/xml/"
files = os.listdir(path)
for xmlFile in files:
  print(xmlFile)