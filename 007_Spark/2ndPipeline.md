# Twitter -> Flume -> HDFS -> Spark -> MySql

### hadoop need to be on
### start-yarn.sh start-dfs.sh
### jps
### Spark cmd
### spark-submit --packages mysql:mysql-connector-java:5.1.39 2ndPipeline.py
### flume send to hdfs cmd
### flume-ng agent --name TwitterAgent --conf-file flume-conf_1stPipeline.properties -Dflume.root.logger=INFO,console
### Create the table first
### CREATE TABLE ht (id INT NOT NULL, hashtag VARCHAR(500) NOT NULL, count INT NOT NULL, length INT NOT NULL, PRIMARY KEY (id));
### hdfs dfs -mkdir /pipeline1
### hdfs dfs -ls /
### MySql connect cmd
### mysql -u sqoop_user -p
### enter your password

### cd $FLUME_HOME/conf/
### gedit flume-conf_1stPipeline.properties
```
# Naming the components on the current agent. 
TwitterAgent.sources = Twitter 
TwitterAgent.channels = MemChannel 
TwitterAgent.sinks = HDFS
# Describing/Configuring the source 
TwitterAgent.sources.Twitter.type = org.apache.flume.source.twitter.TwitterSource
TwitterAgent.sources.Twitter.consumerKey = 
TwitterAgent.sources.Twitter.consumerSecret = 
TwitterAgent.sources.Twitter.accessToken = 
TwitterAgent.sources.Twitter.accessTokenSecret =
TwitterAgent.sources.Twitter.keywords = miami
TwitterAgent.sources.Twitter.language = en
TwitterAgent.sources.Twitter.count = 1000
# Describing/Configuring the sink 
TwitterAgent.sinks.HDFS.type = hdfs 
TwitterAgent.sinks.HDFS.hdfs.path = hdfs://localhost:9000/user/twitter_data/
TwitterAgent.sinks.HDFS.hdfs.fileType = DataStream 
TwitterAgent.sinks.HDFS.hdfs.writeFormat = Text
TwitterAgent.sinks.HDFS.hdfs.fileSuffix = .json 
TwitterAgent.sinks.HDFS.hdfs.batchSize = 1000
TwitterAgent.sinks.HDFS.hdfs.rollSize = 0 
TwitterAgent.sinks.HDFS.hdfs.rollCount = 10000 
# Describing/Configuring the channel 
TwitterAgent.channels.MemChannel.type = memory 
TwitterAgent.channels.MemChannel.capacity = 10000 
TwitterAgent.channels.MemChannel.transactionCapacity = 100
# Binding the source and sink to the channel 
TwitterAgent.sources.Twitter.channels = MemChannel
TwitterAgent.sinks.HDFS.channel = MemChannel 
```