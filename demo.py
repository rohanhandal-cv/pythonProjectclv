            #Connecting to a SQL database and extract data in csv/json format
import mysql.connector
import pandas as pd
#establishing the connection
connection = mysql.connector.connect(user='root', password='Rohan@19',port=3306, database='clvpracties')

#Creating a cursor object using the cursor() method
cursor = connection.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("""DESC employee""")

data = cursor.fetchall()
for i in data:
    print(i)

# creating the dataframe

df = pd.DataFrame(data)
columns = df[0].tolist()
print(columns)

#Executing an MYSQL function using the execute() method

cursor = connection.cursor()
cursor.execute("select * from employee")
data = cursor.fetchall()
for i in data:
    print(i)

df1=pd.DataFrame(data)
df1.columns=columns
print(df1)
df1.to_csv("C:\\Users\\Rohan Handal\\PycharmProjects\\pythonProjectclv\\output\\data.csv",index=False)
