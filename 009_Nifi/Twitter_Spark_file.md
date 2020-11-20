# Ingesting Data from twitter API to File via Spark

## Install Nifi

```
cd Desktop/opt
wget http://archive.apache.org/dist/nifi/1.9.0/nifi-1.9.0-bin.tar.gz
tar zxvf nifi-1.9.0-bin.tar.gz
rm nifi-1.9.0-bin.tar.gz
cd 
gedit .bash_profile
```
### edit .bash_profile
```
## NIFI Home
export NIFI_HOME=/home/consultant/Desktop/opt/nifi-1.9.0
export PATH=$PATH:$NIFI_HOME/bin
```
### source .bash_profile
```
source .bash_profile
```
### start nifi
```
nifi.sh start
```
### see the status of nifi
```
nifi.sh status
```
### if nifi is running, go to localhost:8080/nifi


## On Nifi, create 3 processors
## - GetTwitter
## - ExecuteSparkInteractive
## - PutFile

## GetTwitter Configuration
### Edit 
### - Consumer key 
### - Consumer secret
### - Access Token
### - Access Token Secret

![GetTwitter](https://user-images.githubusercontent.com/54423322/88084701-cc166d00-cb52-11ea-87e5-d141424be5a4.png)

## PutFile Configuration
### Edit Directory (ex: /home/consultant/Desktop/nifi/sink )

![PutFile](https://user-images.githubusercontent.com/54423322/88084794-ec462c00-cb52-11ea-9db9-48a093ca8510.png)

## ExecuteSparkInteractive
### click right, configure
### setting, check-box failure, success, wait
![spark_conf0](https://user-images.githubusercontent.com/54423322/88085639-206e1c80-cb54-11ea-9aea-8d216912cb68.png)

### Properties, click on Livy Controller Service, create new service
![Spark_conf1](https://user-images.githubusercontent.com/54423322/88085816-5dd2aa00-cb54-11ea-9ea3-fbc91e327d7f.png)

![Screenshot from 2020-07-21 13-12-48](https://user-images.githubusercontent.com/54423322/88085913-83f84a00-cb54-11ea-9163-bf322532bcf0.png)

### Click create
### click on the right arrow on the right side of your controller
![spark_controller1](https://user-images.githubusercontent.com/54423322/88086443-637cbf80-cb55-11ea-8633-0ea97365ca63.png)
### click on the setting icon on the right side
![controller_service1](https://user-images.githubusercontent.com/54423322/88086795-ed2c8d00-cb55-11ea-99fe-d1047b43cc3f.png)
### edit Livy host
![controller_setting](https://user-images.githubusercontent.com/54423322/88087020-43013500-cb56-11ea-92f9-4a54dc55009c.png)
### Enable, click on the thunder on the right side
![controller_service2](https://user-images.githubusercontent.com/54423322/88087101-67f5a800-cb56-11ea-91fe-e2c760d4422e.png)
### Start all the processors
![twitter_spark_file](https://user-images.githubusercontent.com/54423322/88087197-8c518480-cb56-11ea-8338-ff386f03c89e.png)

# ---------------------------------------------------------------------


## Option, If you need to add some python code to transform your data, 
## edit spark configuration
![spark_controller_code](https://user-images.githubusercontent.com/54423322/88087432-e05c6900-cb56-11ea-9283-086e3e547edf.png)


## ADD ME A STARS
![stars](https://user-images.githubusercontent.com/54423322/88087651-3af5c500-cb57-11ea-9903-330fd9f86d00.png)

[Samir Benzada](https://github.com/samirbenzada)



