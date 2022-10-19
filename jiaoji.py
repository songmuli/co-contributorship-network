import csv

network1_0=[]
network1_1=[]
network1_2=[]
network1_3=[]
network1_4=[]
network1_5=[]
network1_6=[]
network1_7=[]
network1_8=[]
network1_9=[]
network1_10=[]
network1_11=[]
network1_12=[]
network1_13=[]
network1_14=[]
network1_15=[]
network1_16=[]
network1_17=[]
network1_18=[]
network1_19=[]
network1_20=[]
network1_21=[]
network1_22=[]
network1_23=[]
network1_24=[]
network1_25=[]
network1_26=[]
network1_27=[]
network1_28=[]
network1_29=[]
network1_30=[]
network1_31=[]
network1_32=[]
network1_33=[]
network1_34=[]
network1_35=[]
network1_36=[]
network1_37=[]
network1_38=[]
network1_39=[]
network1_40=[]
network1_41=[]
network1_42=[]
network1_43=[]
network1_44=[]
network1_45=[]
network1_46=[]
network1_47=[]
network1_48=[]
network1_49=[]
network1_50=[]
network1_51=[]
network1_52=[]
network1_53=[]
network1_54=[]
network1_55=[]
network1_56=[]
network1_57=[]
network1_58=[]
network1_59=[]
network1_60=[]
network1_61=[]
network1_62=[]
network1_63=[]
network1_64=[]
network1_65=[]
network1_66=[]
network1_67=[]
network1_68=[]
network1_69=[]
network1_70=[]
network1_71=[]
network1_72=[]
network1_73=[]
network1_74=[]
network1_75=[]
list1 = []
#获取network1各社区的节点
file=open('D:/software/pycharm/xml/network1-id-label-community-1.csv','r')
datasets=csv.reader(file)
for data in datasets:
    if data[3]== '0':
        network1_0.append(data[1])
    if data[3]=='1':
        network1_1.append(data[1])
    if data[3]=='2':
        network1_2.append(data[1])
    if data[3]=='3':
        network1_3.append(data[1])
    if data[3]=='4':
        network1_4.append(data[1])
    if data[3]=='5':
        network1_5.append(data[1])
    if data[3]=='6':
        network1_6.append(data[1])
    if data[3]=='7':
        network1_7.append(data[1])
    if data[3]=='8':
        network1_8.append(data[1])
    if data[3]=='9':
        network1_9.append(data[1])
    if data[3]=='10':
        network1_10.append(data[1])
    if data[3]=='11':
        network1_11.append(data[1])
    if data[3]=='12':
        network1_12.append(data[1])
    if data[3]=='13':
        network1_13.append(data[1])
    if data[3]=='14':
        network1_14.append(data[1])
    if data[3]=='15':
        network1_15.append(data[1])
    if data[3]=='16':
        network1_16.append(data[1])
    if data[3]=='17':
        network1_17.append(data[1])
    if data[3]=='18':
        network1_18.append(data[1])
    if data[3]=='19':
        network1_19.append(data[1])
    if data[3]=='20':
        network1_20.append(data[1])
    if data[3]=='21':
        network1_21.append(data[1])
    if data[3]=='22':
        network1_22.append(data[1])
    if data[3]=='23':
        network1_23.append(data[1])
    if data[3]=='24':
        network1_24.append(data[1])
    if data[3]=='25':
        network1_25.append(data[1])
    if data[3]=='26':
        network1_26.append(data[1])
    if data[3]=='27':
        network1_27.append(data[1])
    if data[3]=='28':
        network1_28.append(data[1])
    if data[3]=='29':
        network1_29.append(data[1])
    if data[3]== '30':
        network1_30.append(data[1])
    if data[3]=='31':
        network1_31.append(data[1])
    if data[3]=='32':
        network1_32.append(data[1])
    if data[3]=='33':
        network1_33.append(data[1])
    if data[3]=='34':
        network1_34.append(data[1])
    if data[3]=='35':
        network1_35.append(data[1])
    if data[3]=='36':
        network1_36.append(data[1])
    if data[3]=='37':
        network1_37.append(data[1])
    if data[3]=='38':
        network1_38.append(data[1])
    if data[3]=='39':
        network1_39.append(data[1])
    if data[3]=='40':
        network1_40.append(data[1])
    if data[3]=='41':
        network1_41.append(data[1])
    if data[3]=='42':
        network1_42.append(data[1])
    if data[3]=='43':
        network1_43.append(data[1])
    if data[3]=='44':
        network1_44.append(data[1])
    if data[3]=='45':
        network1_45.append(data[1])
    if data[3]=='46':
        network1_46.append(data[1])
    if data[3]=='47':
        network1_47.append(data[1])
    if data[3]=='48':
        network1_48.append(data[1])
    if data[3]=='49':
        network1_49.append(data[1])
    if data[3]=='50':
        network1_50.append(data[1])
    if data[3]=='51':
        network1_51.append(data[1])
    if data[3]=='52':
        network1_52.append(data[1])
    if data[3]=='53':
        network1_53.append(data[1])
    if data[3]=='54':
        network1_54.append(data[1])
    if data[3]=='55':
        network1_55.append(data[1])
    if data[3]=='56':
        network1_56.append(data[1])
    if data[3]=='57':
        network1_57.append(data[1])
    if data[3]=='58':
        network1_58.append(data[1])
    if data[3]=='59':
        network1_59.append(data[1])
    if data[3]== '60':
        network1_60.append(data[1])
    if data[3]=='61':
        network1_61.append(data[1])
    if data[3]=='62':
        network1_62.append(data[1])
    if data[3]=='63':
        network1_63.append(data[1])
    if data[3]=='64':
        network1_64.append(data[1])
    if data[3]=='65':
        network1_65.append(data[1])
    if data[3]=='66':
        network1_66.append(data[1])
    if data[3]=='67':
        network1_67.append(data[1])
    if data[3]=='68':
        network1_68.append(data[1])
    if data[3]=='69':
        network1_69.append(data[1])
    if data[3]== '70':
        network1_70.append(data[1])
    if data[3]=='71':
        network1_71.append(data[1])
    if data[3]=='72':
        network1_72.append(data[1])
    if data[3]=='73':
        network1_73.append(data[1])
    if data[3]=='74':
        network1_74.append(data[1])
    if data[3]=='75':
        network1_75.append(data[1])
print(len(network1_11))
print(len(network1_26))
list1.append(network1_0)
list1.append(network1_1)
list1.append(network1_2)
list1.append(network1_3)
list1.append(network1_4)
list1.append(network1_5)
list1.append(network1_6)
list1.append(network1_7)
list1.append(network1_8)
list1.append(network1_9)
list1.append(network1_10)
list1.append(network1_11)
list1.append(network1_12)
list1.append(network1_13)
list1.append(network1_14)
list1.append(network1_15)
list1.append(network1_16)
list1.append(network1_17)
list1.append(network1_18)
list1.append(network1_19)
list1.append(network1_20)
list1.append(network1_21)
list1.append(network1_22)
list1.append(network1_23)
list1.append(network1_24)
list1.append(network1_25)
list1.append(network1_26)
list1.append(network1_27)
list1.append(network1_28)
list1.append(network1_29)
list1.append(network1_30)
list1.append(network1_31)
list1.append(network1_32)
list1.append(network1_33)
list1.append(network1_34)
list1.append(network1_35)
list1.append(network1_36)
list1.append(network1_37)
list1.append(network1_38)
list1.append(network1_39)
list1.append(network1_40)
list1.append(network1_41)
list1.append(network1_42)
list1.append(network1_43)
list1.append(network1_44)
list1.append(network1_45)
list1.append(network1_46)
list1.append(network1_47)
list1.append(network1_48)
list1.append(network1_49)
list1.append(network1_50)
list1.append(network1_51)
list1.append(network1_52)
list1.append(network1_53)
list1.append(network1_54)
list1.append(network1_55)
list1.append(network1_56)
list1.append(network1_57)
list1.append(network1_58)
list1.append(network1_59)
list1.append(network1_60)
list1.append(network1_61)
list1.append(network1_62)
list1.append(network1_63)
list1.append(network1_64)
list1.append(network1_65)
list1.append(network1_66)
list1.append(network1_67)
list1.append(network1_68)
list1.append(network1_69)
list1.append(network1_70)
list1.append(network1_71)
list1.append(network1_72)
list1.append(network1_73)
list1.append(network1_74)
list1.append(network1_75)
print('已得到network1各社区的节点ID....')
print(list1)
print(len(list1))


network2_0 = []
network2_1 = []
network2_2 = []
network2_3 = []
network2_4 = []
network2_5 = []
network2_6 = []
network2_7 = []
network2_8 = []
network2_9 = []
network2_10 = []
network2_11 = []
network2_12 = []
network2_13 = []
network2_14 = []
network2_15 = []
network2_16 = []
network2_17 = []
network2_18 = []
network2_19 = []
network2_20 = []
network2_21 = []
network2_22 = []
network2_23 = []
network2_24 = []
network2_25 = []
network2_26 = []
network2_27 = []
network2_28 = []
network2_29 = []
network2_30=[]
network2_31=[]
network2_32=[]
network2_33=[]
network2_34=[]
network2_35=[]
network2_36=[]
network2_37=[]
network2_38=[]
network2_39=[]
network2_40=[]
network2_41=[]
network2_42=[]
network2_43=[]
network2_44=[]
network2_45=[]
network2_46=[]
network2_47=[]
network2_48=[]
network2_49=[]
network2_50=[]
network2_51=[]
network2_52=[]
network2_53=[]
network2_54=[]
network2_55=[]
network2_56=[]
network2_57=[]
network2_58=[]
network2_59=[]
network2_60=[]
network2_61=[]
network2_62=[]
network2_63=[]
network2_64=[]
network2_65=[]
network2_66=[]
network2_67=[]
network2_68=[]
network2_69=[]
network2_70=[]
network2_71=[]
network2_72=[]
network2_73=[]
network2_74=[]
network2_75=[]
network2_76=[]
network2_77=[]
network2_78=[]
network2_79=[]
network2_80=[]
network2_81=[]
network2_82=[]
network2_83=[]
network2_84=[]
list2=[]
# 获取network1各社区的节点
file = open('D:/software/pycharm/xml/network2-id-label-community.csv', 'r')
datasets = csv.reader(file)
for data in datasets:
    if data[3] == '0':
        network2_0.append(data[1])
    if data[3] == '1':
        network2_1.append(data[1])
    if data[3] == '2':
        network2_2.append(data[1])
    if data[3] == '3':
        network2_3.append(data[1])
    if data[3] == '4':
        network2_4.append(data[1])
    if data[3] == '5':
        network2_5.append(data[1])
    if data[3] == '6':
        network2_6.append(data[1])
    if data[3] == '7':
        network2_7.append(data[1])
    if data[3] == '8':
        network2_8.append(data[1])
    if data[3] == '9':
        network2_9.append(data[1])
    if data[3] == '10':
        network2_10.append(data[1])
    if data[3] == '11':
        network2_11.append(data[1])
    if data[3] == '12':
        network2_12.append(data[1])
    if data[3] == '13':
        network2_13.append(data[1])
    if data[3] == '14':
        network2_14.append(data[1])
    if data[3] == '15':
        network2_15.append(data[1])
    if data[3] == '16':
        network2_16.append(data[1])
    if data[3] == '17':
        network2_17.append(data[1])
    if data[3] == '18':
        network2_18.append(data[1])
    if data[3] == '19':
        network2_19.append(data[1])
    if data[3] == '20':
        network2_20.append(data[1])
    if data[3] == '21':
        network2_21.append(data[1])
    if data[3] == '22':
        network2_22.append(data[1])
    if data[3] == '23':
        network2_23.append(data[1])
    if data[3] == '24':
        network2_24.append(data[1])
    if data[3] == '25':
        network2_25.append(data[1])
    if data[3] == '26':
        network2_26.append(data[1])
    if data[3] == '27':
        network2_27.append(data[1])
    if data[3] == '28':
        network2_28.append(data[1])
    if data[3] == '29':
        network2_29.append(data[1])
    if data[3] == '30':
        network2_30.append(data[1])
    if data[3] == '31':
        network2_31.append(data[1])
    if data[3] == '32':
        network2_32.append(data[1])
    if data[3] == '33':
        network2_33.append(data[1])
    if data[3] == '34':
        network2_34.append(data[1])
    if data[3] == '35':
        network2_35.append(data[1])
    if data[3] == '36':
        network2_36.append(data[1])
    if data[3] == '37':
        network2_37.append(data[1])
    if data[3] == '38':
        network2_38.append(data[1])
    if data[3] == '39':
        network2_39.append(data[1])
    if data[3] == '40':
        network2_40.append(data[1])
    if data[3] == '41':
        network2_41.append(data[1])
    if data[3] == '42':
        network2_42.append(data[1])
    if data[3] == '43':
        network2_43.append(data[1])
    if data[3] == '44':
        network2_44.append(data[1])
    if data[3] == '45':
        network2_45.append(data[1])
    if data[3] == '46':
        network2_46.append(data[1])
    if data[3] == '47':
        network2_47.append(data[1])
    if data[3] == '48':
        network2_48.append(data[1])
    if data[3] == '49':
        network2_49.append(data[1])
    if data[3] == '50':
        network2_50.append(data[1])
    if data[3] == '51':
        network2_51.append(data[1])
    if data[3] == '52':
        network2_52.append(data[1])
    if data[3] == '53':
        network2_53.append(data[1])
    if data[3] == '54':
        network2_54.append(data[1])
    if data[3] == '55':
        network2_55.append(data[1])
    if data[3] == '56':
        network2_56.append(data[1])
    if data[3] == '57':
        network2_57.append(data[1])
    if data[3] == '58':
        network2_58.append(data[1])
    if data[3] == '59':
        network2_59.append(data[1])
    if data[3] == '60':
        network2_60.append(data[1])
    if data[3] == '61':
        network2_61.append(data[1])
    if data[3] == '62':
        network2_62.append(data[1])
    if data[3] == '63':
        network2_63.append(data[1])
    if data[3] == '64':
        network2_64.append(data[1])
    if data[3] == '65':
        network2_65.append(data[1])
    if data[3] == '66':
        network2_66.append(data[1])
    if data[3] == '67':
        network2_67.append(data[1])
    if data[3] == '68':
        network2_68.append(data[1])
    if data[3] == '69':
        network2_69.append(data[1])
    if data[3] == '70':
        network2_70.append(data[1])
    if data[3] == '71':
        network2_71.append(data[1])
    if data[3] == '72':
        network2_72.append(data[1])
    if data[3] == '73':
        network2_73.append(data[1])
    if data[3] == '74':
        network2_74.append(data[1])
    if data[3] == '75':
        network2_75.append(data[1])
    if data[3] == '76':
        network2_76.append(data[1])
    if data[3] == '77':
        network2_77.append(data[1])
    if data[3] == '78':
        network2_78.append(data[1])
    if data[3] == '79':
        network2_79.append(data[1])
    if data[3] == '80':
        network2_80.append(data[1])
    if data[3] == '81':
        network2_81.append(data[1])
    if data[3] == '82':
        network2_82.append(data[1])
    if data[3] == '83':
        network2_83.append(data[1])
    if data[3] == '84':
        network2_84.append(data[1])
list2.append(network2_0)
list2.append(network2_1)
list2.append(network2_2)
list2.append(network2_3)
list2.append(network2_4)
list2.append(network2_5)
list2.append(network2_6)
list2.append(network2_7)
list2.append(network2_8)
list2.append(network2_9)
list2.append(network2_10)
list2.append(network2_11)
list2.append(network2_12)
list2.append(network2_13)
list2.append(network2_14)
list2.append(network2_15)
list2.append(network2_16)
list2.append(network2_17)
list2.append(network2_18)
list2.append(network2_19)
list2.append(network2_20)
list2.append(network2_21)
list2.append(network2_22)
list2.append(network2_23)
list2.append(network2_24)
list2.append(network2_25)
list2.append(network2_26)
list2.append(network2_27)
list2.append(network2_28)
list2.append(network2_29)
list2.append(network2_30)
list2.append(network2_31)
list2.append(network2_32)
list2.append(network2_33)
list2.append(network2_34)
list2.append(network2_35)
list2.append(network2_36)
list2.append(network2_37)
list2.append(network2_38)
list2.append(network2_39)
list2.append(network2_40)
list2.append(network2_41)
list2.append(network2_42)
list2.append(network2_43)
list2.append(network2_44)
list2.append(network2_45)
list2.append(network2_46)
list2.append(network2_47)
list2.append(network2_48)
list2.append(network2_49)
list2.append(network2_50)
list2.append(network2_51)
list2.append(network2_52)
list2.append(network2_53)
list2.append(network2_54)
list2.append(network2_55)
list2.append(network2_56)
list2.append(network2_57)
list2.append(network2_58)
list2.append(network2_59)
list2.append(network2_60)
list2.append(network2_61)
list2.append(network2_62)
list2.append(network2_63)
list2.append(network2_64)
list2.append(network2_65)
list2.append(network2_66)
list2.append(network2_67)
list2.append(network2_68)
list2.append(network2_69)
list2.append(network2_70)
list2.append(network2_71)
list2.append(network2_72)
list2.append(network2_73)
list2.append(network2_74)
list2.append(network2_75)
list2.append(network2_76)
list2.append(network2_77)
list2.append(network2_78)
list2.append(network2_79)
list2.append(network2_80)
list2.append(network2_81)
list2.append(network2_82)
list2.append(network2_83)
list2.append(network2_84)
print('已得到network2各社区的节点....')
print(list2)
print(len(list2))
#
#

#两个集合相似度
results = []
for id1,value1 in enumerate(list1):
 for id2,value2 in enumerate(list2):
   jiaoji = set(value1) & set(value2)
   bingji = set(value1) | set(value2)
   similarity= len(jiaoji) / len(bingji)
   if len(jiaoji) > 0:
     tuple1=(id1,id2,len(jiaoji),similarity)
     results.append(tuple1)

import pandas as pd
data=pd.DataFrame(results)
data.to_csv('D:/2022bishe/过程文档/images/venn/conclusion.csv',sep='\t',index=0,header=0)


#
# print('开始画两集合的韦恩图....')
# import matplotlib.pyplot as plt
# from matplotlib_venn import venn2
# my_dpi = 96
# plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
# venn2([set(network1_11), set(network1_12)])
# plt.show()

# # #画桑基图
# import pandas as pd
#
# file = "D:/2022bishe/过程文档/images/venn/conclusion-1.xlsx"
# data = pd.read_excel(file)
# df = pd.DataFrame(data)
# print(df)
#
# nodes=[]
#
# for i in range(2):
#     values=df.iloc[:,i].unique()
#     for value in values:
#         dic={}
#         dic['name']=value
#         nodes.append(dic)
# print(nodes)
#
# links=[]
# for i in df.values:
#     dic={}
#     dic['source']=i[0]
#     dic['target']=i[1]
#     dic['value']=i[2]
#     links.append(dic)
# print(links)
# print(len(links))
#
# from pyecharts.charts import Sankey
# from pyecharts import options as opts
# pic = (
#     Sankey()
#     .add('', #图例名称
#          nodes,    #传入节点数据
#          links,   #传入边和流量数据
#          #设置透明度、弯曲度、颜色
#          linestyle_opt=opts.LineStyleOpts(opacity = 0.3, curve = 0.5, color = "source"),
#          #标签显示位置
#          label_opts=opts.LabelOpts(position="right"),
#          #节点之前的距离
#          node_gap = 30,
#     )
#     .set_global_opts(title_opts=opts.TitleOpts(title = 'Comparison of results of community division'))
# )
#
# pic.render('test.html')




