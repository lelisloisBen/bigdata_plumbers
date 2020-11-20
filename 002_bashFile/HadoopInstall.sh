#!/bin/sh

echo "INSTALLING HADOOP"
echo
echo

# sudo apt-get update (change the password of your computer)
echo "DOING UPDATE FIRST"
sudo apt-get update << EOF
Welcome2BB
EOF
echo
echo

# create a directory opt on Desktop ( mkdir -p if don't exist )
echo "CREATING OPT DIRECTORY"
cd
cd Desktop
mkdir -p opt
cd opt



# Download Hadoop

echo "DOWNLOADING HADOOP"
wget http://apache.mirrors.hoobly.com/hadoop/common/current/hadoop-3.1.3.tar.gz

# Unzip the Hadoop file
echo "UNZIP HADOOP"
tar -zxvf hadoop-3.1.3.tar.gz

## remove hadoop tar

# create bash profile (at the root) if don't exist. Open it if exist.
echo "CREATING BASH PROFILE"
cd
sudo gedit .bash_profile << EOF
Welcome2BB
EOF

## Set up Hadoop Home
echo "export HADOOP_HOME=/home/tammy/opt/hadoop" >> .bash_profile.sh
echo "export HADOOP_INSTALL=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_MAPRED_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_HDFS_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export YARN_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native" >> .bash_profile.sh
echo "export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin" >> .bash_profile.sh

# set up hadoop configuration file
echo "SETUP HADOOP FILES"
cd
cd Desktop/opt/hadoop/etc/hadoop
sudo gedit hadoop-env.sh  << EOF
Welcome2BB
EOF

echo "export JAVA_HOME=/usr/lib/jvm/java-11-oracle" >> hadoop-env.sh

## Edit core-site.xml
echo "EDITING CORE-SITE.XML"
sudo gedit core-site.xml << EOF
Welcome2BB
EOF

echo "<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>
</configuration>" >> core-site.xml

## Edit hdfs-site.xml
echo "EDITING HDFS-SITE.XML"
sudo gedit hdfs-site.xml << EOF
Welcome2BB
EOF
echo "<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>
<property>
  <name>dfs.name.dir</name>
    <value>file:/home/consultant/Desktop/opt/hadoop-3.1.3/hdfs/namenode</value>
</property>
<property>
  <name>dfs.data.dir</name>
    <value>file:/home/consultant/Desktop/opt/hadoop-3.1.3/hdfs/datanode</value>
</property>
configuration>" >> hdfs-site.xml

## Edit mapred-site.xml
echo "EDITING MAPRED-SITE.XML"
sudo gedit mapred-site.xml << EOF
Welcome2BB
EOF
echo "<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>

<property>
   <name>yarn.app.mapreduce.am.env</name>
   <value>HADOOP_MAPRED_HOME=/home/consultant/Desktop/opt/hadoop-3.1.3</value>
</property>

<property>
   <name>mapreduce.map.env</name>
   <value>HADOOP_MAPRED_HOME=/home/consultant/Desktop/opt/hadoop-3.1.3</value>
</property>

<property>
   <name>mapreduce.reduce.env</name>
   <value>HADOOP_MAPRED_HOME=/home/consultant/Desktop/opt/hadoop-3.1.3</value>
</property>

<property> 
    <name>mapreduce.application.classpath</name>
    <value>/home/consultant/Desktop/opt/hadoop-3.1.3/etc/hadoop:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/common/lib/*:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/common/*:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/hdfs:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/hdfs/lib/*:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/hdfs/*:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/mapreduce/lib/*:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/mapreduce/*:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/yarn:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/yarn/lib/*:/home/consultant/Desktop/opt/hadoop-3.1.3/share/hadoop/yarn/*
</value>
</property>
</configuration>" >> mapred-site.xml

## Edit yarn-site.xml
echo "EDITING YARN-SITE.XML"
sudo gedit yarn-site.xml << EOF
Welcome2BB
EOF
echo "<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>
</configuration>" >> yarn-site.xml

## Source bash profile ( at root )
echo "SOURCE BASH_PROFILE"
cd
source .bash_profile

## Format HDFS Namenode ( at root )
echo "FORMAT HDFS"
cd
hdfs namenode -format

## Start all sh ( at root ) start-all.sh is not always working so start yarn and dfs.
echo "STARTING YARN AND DFS"
cd
start-yarn.sh
start-dfs.sh

## verify if everything is running
echo "CHECKING JPS"
jps





