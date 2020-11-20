# How to create a connexion with netcat

### example on same machine, open two terminals.
### in the first terminal enter this command
### nc stand for netcat, localhost for the server, 9600 is the port you choose, -l for listenner
```
nc localhost 9600 -l
```
### the other machine will enter this
```
nc localhost 9600
```

### now in two machine with separte ip address  
### find the ip address first (look at the 2nd or 3rd like wlo1: inet 192.168.0.129)
``` 
ip address
```
### then enter netcat command
```
nc 192.168.0.129 9600 -l
```
### do the same in the other computer terminal
```
nc 192.168.0.129 9600
```

### Use the following format to communicate between 2 Virtual Machines

```
sudo service ssh start
ssh-keygen
On VM1- ssh "user@IP Address of VM2"
On VM1- nc  localhost <Port>
On VM2- nc -l <Port>
sudo service ssh stop
```

