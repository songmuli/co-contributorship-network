import csv

communityID=[]
file=open('D:/software/pycharm/xml/network2-id-label-community.csv','r')
datasets=csv.reader(file)
for data in datasets:
    communityID.append(data[2])
# print(communityID)
int_communityID=[]
for i in communityID:
    int_communityID.append(int(i))
# print(int_communityID)

#统计各社区的节点数
dict={}
for key in int_communityID:
    dict[key] = dict.get(key, 0) + 1
print(dict)

#绘图，横轴为键，纵轴为值
X=[]
Y=[]
for k,v in dict.items():
    X.append(k)
    Y.append(v)
# print(X)
# print(Y)
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.bar(X,Y,color = '#9999ff',width = 0.5)
plt.title('Number of nodes per community')
plt.xlabel('communityID')
plt.ylabel('number of nodes')
plt.xticks(X)
plt.tick_params(labelsize=6)
plt.show()