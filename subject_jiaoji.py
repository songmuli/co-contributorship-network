import pymysql

first_subject_type = []
second_subject_type = []

db = pymysql.connect(host='localhost', user='root', password='123456', db='bishe')
print("数据库连接成功！")
cursor = db.cursor()

cursor.execute("SELECT DISTINCT first_subject FROM subject_static")
result_1 = cursor.fetchall()
for res_1 in result_1:
    first_subject_type.append(res_1[0])
for f_subject in first_subject_type:
    temp_subject = []
    cursor.execute('SELECT doi FROM subject_static where first_subject = %s ', (f_subject))
    result = cursor.fetchall()
    for res in result:
        temp_subject.append(res[0])
    


# cursor.execute("SELECT DISTINCT first_subject,second_subject FROM subject_static")
# result_2 = cursor.fetchall()
# for res_2 in result_1:
#     second_subject_type.append(res_2[0])

