import xml.etree.cElementTree as ET
import os
import os.path
import openpyxl

# path = 'D:/2022bishe/pbio/file@id=10.1371%2Fjournal.pbio.1002332&type=manuscript'
path = 'D:/2022bishe/pbio/'
files = os.listdir(path)
for xmlFile in files:
  tree = ET.parse(os.path.join(path, xmlFile))
  root = tree.getroot()
  contribs = root.findall("./front/article-meta/contrib-group/contrib")
  affs = root.findall("./front/article-meta/aff")
# for aff in affs:
#     addr = aff.find("./addr-line").text
#     print(addr)
  author_dict = {}
  for contrib in contribs:
    if contrib.attrib['contrib-type'] == 'author':
       surnames = contrib.find("./name/surname").text
       given_names = contrib.find("./name/given-names").text
       names = given_names + ' ' + surnames
      # print(names)
       addr_line = []
       addr = ''
       xrefs = contrib.findall("./xref")
       for xref in xrefs:
        # if xref.attrib["ref-type"] == 'corresp':
        #    corresp_author.append(names)
        if xref.attrib["ref-type"] == 'aff':
          rid = xref.attrib['rid']
          for aff in affs:
           if aff.attrib["id"] == rid:
            addr_line.append(aff.find("./addr-line").text)
          addr = ' ; '.join(str(addrline) for addrline in addr_line)
      # print("names: %s ; addr: %s " % (names, addr))
       author_dict.update({names: addr})
  print(author_dict)
  print(xmlFile)
