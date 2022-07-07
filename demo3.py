#3. Take any sample data, create dataframes using pandas library, apply some transformations and store in SQL database

import pandas as pd
import mysql.connector
from datetime import datetime
df=pd.read_csv("C:\\Users\\Rohan Handal\\PycharmProjects\\pythonProjectclv\\output\\data.csv")
df['Date_time'] = datetime.now().date()
df['Unique_id'] = df.Name +"_"+df.Dept
print(df)
dataf1 = [tuple(i) for i in df.values ]
print(dataf1)

with mysql.connector.connect(user='root', password='Rohan@19', port=3306, database='clvpracties') as conn:
    with conn.cursor() as cursor:
        cursor.execute("drop table if exists Student")
        cursor.execute("CREATE TABLE Student (Empid int,Name varchar(20),Dept varchar(20),Salary int,Date_time datetime,Unique_id varchar(200))")
        for i in dataf1:
            cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s)", i)
    conn.commit()

