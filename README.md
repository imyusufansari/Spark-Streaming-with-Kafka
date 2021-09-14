# Building a real-time data streaming application with Apache Kafka

## Project Description

Real-Time Meetup RSPV Data Processing from https://www.meetup.com/. Real-Time Analytics using Apache Kafka, Zookeeper, Py Spark. Analyzing the real time RSVP data of meetup.com to get real-time insights such as trending topics, cities etc. along with other business insights related to Meetups RSVPs. The data processing scripts are developed in Python.

Getting this streaming data into Apache Spark-Streaming is the first step to perform various analytics, recommendations or visualizations on the data.

## Technologies Used

* Spark 3.1.2
* Kafka 2.8.0
* PySpark 2.4.8
* Python 3.6
* Data Feeds: kafka-python 2.0.2
* ETL: Spark DataFrame, Spark Structured Streaming
* Visualization: matplotlib 3.4.3
* Git/GitHub 

[Kafka Python API](https://github.com/dpkp/kafka-python) is used to interact with kafka cluster. PySpark is used to write the spark streaming jobs.

# Features

List of features ready and TODOs for future development
```
1. What are the current active cities in US which are scheduling Meetup Events?
2. What are the trending topics in US Meetup Events?
3. How many Big data Meetup Events events scheduled in each country?
```

## Getting Started

Assuming Kafka and Spark of appropriate version is installed, the following commands are used to run the application.

> Spark Streaming integeration with kafka 0.10.0.0 and above.

1. Run Zookeeper to maintain Kafka, command to be run from Kafka root dir
```
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```

2. Start Kafka server, aditional servers can be added as per requirement.
```
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

3. Start Producer.py to start reading data from the meetup stream and store it in '''meetup''' kafka topic.

4. Start Consumer notebook to consume the processed stream from the spark streaming.

5. Submit the spark job <spark_file>.py, to read the data into Spark Streaming from Kafka.
> Spark depends on a external package for kafka integeration [link](https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-10_2.12/3.1.2)
```
bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 spark_meetup.py localhost:2181 meetup
```

6. Start <consumer_file>.ipynb file to visualize the data.

# License
This project uses the following license: [Apache License 2.0](https://github.com/myusufuc/Spark-Streaming-with-Kafka/blob/f8f1af71e1e2346140cf447e8254ce7e2354026f/LICENSE)

# References

* https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10_2.12/3.1.2)
* http://spark.apache.org/docs/latest/streaming-kafka-integration.html
* https://stream.meetup.com/2/rsvps

