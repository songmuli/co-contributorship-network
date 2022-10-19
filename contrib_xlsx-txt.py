import pandas as pd

df = pd.read_excel('D:/2022bishe/pone-1.xlsx')
# print(type(df))
df.to_csv('D:/2022bishe/total/txt/pone2_g+s.txt', index=False, sep=',', encoding='utf_8_sig')
# cols = df.shape[1]
# print(rows)
# print(cols)



