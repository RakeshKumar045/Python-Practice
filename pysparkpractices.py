from pyspark.sql import SparkSession ,lit
spark1 = SparkSession.biulder.appName("hello").getOrCreate()

d1 = {"Name":["Natasha","meenu","tinu","Puchu","kuchu","tilu"],
"age":[6,13,63,17,18,21],
      "city":["pune","kolkata","goa","up","mp","pune"]
      }
df = spark1.createDataFrame(d1)
df.show()

df.columns
df.count()
df.describe()
df.filter(df["Name"]=="meenu").show()
df.trim("")
df.withcolumn(df["salary"],df["name"])
df.withcolumnRenamed("salary","earning").withcolumnrenamed("Name","customer")
df.withcolun("state",lit("good"))
df.dropDuplicates()
df.dropDuplicates("name")
df.isnull()
df.isnall.sum()
df.fillna()
df.na.fill()
df.bfill()
df.ffill()
df.filter(df["name"]=="miku").show()
df.groupBy("salary").sum().orderby desc
df.when(df["salary"]=="1000")

