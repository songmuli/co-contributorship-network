import pandas as pd
import csv
import jieba

all_articles_keywords = []
for i in range(17):
    file1_name=str(i+1)+'.txt'
    count=0
    with open('D:/software/pycharm/xml/network1-community30/title+abstract/'+file1_name,'r', encoding='utf-8') as f:
        content=f.read()
        content = content.replace(',', ' ')
        content = content.replace('.', ' ')
        content = content.replace('!', ' ')
        content = content.replace('-', ' ')
        content = content.replace('_', ' ')
        content = content.replace('(', ' ')
        content = content.replace(')', ' ')
        content = content.strip()
        words = [word.lower() for word in content.split()]
        print(len(words))
