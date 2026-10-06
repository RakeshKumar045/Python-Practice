import pandas as pd
from sqlachemy import create engine

# print("hello world")
# print("dekha ho gya na ha ha ha ....")

# print (" aata ha mujhe sab kuch ")
#
# a=10
# b=20
# try :
#     print(addition,a+b)
#
# except:
#     print(" this is may be true")
# finally:
#     print("excute the program ")
#
#     print("ok")

data = (("Natasha",15,1),("pankaj",17,6),("ritu",25,2)
,("santosh",30,4),("samir",22,5))

col = ("Name","Age","ID")

df = pd.DataFrame(data = data, columns=col)
print(df.head())
df2 = df.to_csv("rakeshhello.csv",index=False)
# df1 = df.to_csv(df)

engine =create_engine("mysql+mysqlconnection://root:Test1234!%@localhost/mysql")

table_name =loannik
df=pd.read_csv("rakeshhello.csv")
df.to_sql(name=table_name,con=engine,if_exists="replace",index=False)

engine.dospose()


