#!/bin/sh

echo "STOPING KAFKA"
kafka-server-stop.sh

echo "WAITING FOR KAFKA TO STOP..."

sleep 10

echo "KAFKA STOPED"
echo "STOPING ZOOKEPER"

zookeeper-server-stop.sh

echo "WAITING FOR ZOOKEEPER TO STOP..."
sleep 10

stop-all.sh

echo "STOPPED !!!" 
