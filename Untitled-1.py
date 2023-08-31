from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.getActiveSession()

df = spark.sql('select * from samples.tpch.orders limit 10')

df.show()