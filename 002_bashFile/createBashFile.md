# How to create a Bash File for automatic execution

## at root level

```
sudo gedit test.sh
```

## inside the test.sh write this at the top
```
#!/bin/sh
```

## then write your command for example for update
```
sudo apt-get update
```

## To run a bash file you can run two different commands
```
bash test.sh
```
or
```
. test.sh
```

