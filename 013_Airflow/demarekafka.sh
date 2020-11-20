#!/bin/sh

RED='\033[1;31m'
BLUE='\033[0;34m'
Y='\033[1;33m'
G='\033[0;33m'
P='\033[035m'

echo -e "${Y}######################"
echo -e "${BLUE}STARTING ${BLUE}ZOOKEEPER"
echo -e "${Y}######################"

zookeeper-server-start.sh -daemon $KAFKA_HOME/config/zookeeper.properties

echo -e "${P}######################"
echo -e "${G}WAITING ${G}FOR ${G}ZOOKEEPER ${G}TO ${G}START..."
echo -e "${P}######################"

sleep 10

echo -e "${Y}######################"
echo -e "${BLUE}STARTING ${BLUE}KAFKA"
echo -e "${Y}######################"

kafka-server-start.sh -daemon $KAFKA_HOME/config/server_capstone.proporties

echo -e "${P}######################"
echo -e "${G}WAITING ${G}FOR ${G}KAFKA ${G}TO ${G}START..."
echo -e "${P}######################"

sleep 10

echo -e "${Y}######################"
echo -e "${BLUE}KAFKA ${BLUE}STARTED..."
echo -e "${Y}######################"

echo -e "${P}######################"
echo -e "${G}START ${G}YARN"
echo -e "${P}######################"

start-yarn.sh

echo -e "${Y}######################"
echo -e "${BLUE}START ${BLUE}HDFS"
echo -e "${Y}######################"

start-dfs.sh

echo -e "${P}######################"
echo -e "${RED}ALL ${RED}DONE ${RED}SAMIR"
echo -e "${P}######################"


