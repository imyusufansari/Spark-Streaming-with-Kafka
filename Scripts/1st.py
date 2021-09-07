# What are the current active cities in India which are scheduling Meetup Events?


# ./pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2

# Import Required Libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_json, struct
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

raw_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sample") \
    .option("startingOffsets", "latest") \
    .load() \
    .selectExpr("CAST(value AS STRING)")

schema = StructType(
    [
        StructField("venue", StructType([
            StructField("venue_name", StringType()),
            StructField("lon", FloatType()),
            StructField("lat", FloatType()),
            StructField("venue_id", IntegerType())]
        )), 
        StructField("visibility", StringType()),
        StructField("response", StringType()),
        StructField("guests", IntegerType()),
        StructField("member", StructType([
            StructField("member_id", IntegerType()),
            StructField("photo", StringType()),
            StructField("member_name", StringType()),]
        )),
        StructField("rsvp_id", IntegerType()),
        StructField("mtime", TimestampType()),
        StructField("event", StructType([
            StructField("event_name", StringType()),
            StructField("event_id", StringType()),
            StructField("time", TimestampType()),
            StructField("event_url", StringType()),]
        )),

        StructField("group", StructType([
            StructField("group_topics", ArrayType(
                StructType([
                    StructField("urlkey", StringType()),
                    StructField("topic_name", StringType()),]
                )
            )),
            StructField("group_city", StringType()),
            StructField("group_country", StringType()),
            StructField("group_id", IntegerType()),
            StructField("group_name", StringType()),
            StructField("group_lon", FloatType()),
            StructField("group_urlname", StringType()),
            StructField("group_lat", FloatType()),  
        ])),              
    ]
)

schema_df = raw_df.select(from_json(raw_df.value, schema).alias("data"))
us_df = schema_df.filter(col("data.group.group_country") == 'us')
city_df = us_df.select(col("data.group.group_city").alias("city"))
sql = city_df.writeStream.outputMode("append").format('memory').queryName('this_query').start()
output = spark.sql("select city, count(*) as city_count from this_query group by city order by city_count desc")

output_df = (output.select(to_json(struct(col("*"))).alias("value")))

output_df.write.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("topic", "output").save()

