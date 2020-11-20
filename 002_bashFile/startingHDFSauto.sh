#!/bion/sh

echo "starting hdfs automatically"
echo
echo

# sudo apt-get update (change the password of your computer)
echo "DOING UPDATE FIRST"
sudo apt-get update << EOF
Welcome2BB
EOF
echo
echo

# start hdfs
echo "DOING SOURCE .BASH_PROFILE" 
source .bash_profile
echo
echo

echo "DOING HDFS NAMENODE -FORMAT"
hdfs namenode -format << EOF
y
EOF
echo
echo

echo "STARTING ALL SH"
start-all.sh
echo
echo

# jps check
echo "JPS -- CHECKING JAVA PROCESS STATUS"
jps