from pyspark import SparkContext
from pyspark.sql import SparkSession
import json
import sys
import imaplib
import getpass
import email
import re

# spark-submit --packages mysql:mysql-connector-java:5.1.39 spark_gmail.py 

sc = SparkContext(appName="GmailToMySQL")
spark = SparkSession(sc)

data_list = []

def toSQL(df):
	df.show()
	df.write.format("jdbc")\
	.mode("overwrite")\
	.option("url", "jdbc:mysql://localhost:3306/hadoop_test") \
	.option("dbtable", "gmail_table") \
	.option("user", "sqoop_user") \
	.option("password", "Welcome2BB") \
	.option("driver", "com.mysql.jdbc.Driver") \
	.save()


### Read Emails from Gmail Account

M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    M.login('enhanceit.test@gmail.com', "Welcome2BB")
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")
rv, mailboxes = M.list()
def process_mailbox(M):
  rv, data = M.search(None, "UNSEEN") 
  if rv != 'OK':
      print("No messages found!")
      return
  for num in data[0].split():
      rv, data = M.fetch(num, '(RFC822)')
      if rv != 'OK':
          print("ERROR getting message", num)
          return
      dict_num = {}
      msg = email.message_from_string(data[0][1].decode('utf-8'))
      dict_num['From'] = msg['From']
      subject = msg['Subject']
      mess = subject.replace("Fwd: ", "")
      dict_num["Message"] = mess
      dict_num['Date:'] = msg['Date']

      if msg.is_multipart():
          for part in msg.walk():
              content_type = part.get_content_type()
              content_disposition = str(part.get('content disposition'))
            
              if content_type == "text/plain" and "attachment" not in content_disposition:
                  body = part.get_payload().decode()
                  newBody = body.replace("\r\n"," ").replace("*","").replace(" : ", ": ").replace("\u2022", "0.").replace('Responsibility',"Description")\
                                .replace("- ", "0.").replace("Tittle","Title").replace("Contract:","Type:")
                  phone = r"\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}"
                  myPhone = re.findall(phone, newBody)
                  
                  dict_num['PhoneNumber'] = ""

                  for phoneNum in myPhone:
                      if len(myPhone) > 1:
                          dict_num['PhoneNumber'] += phoneNum + ", "
                      else:
                          dict_num['PhoneNumber'] = phoneNum

                  regex_pattern = r"Title:\s\w+ \w+"
                  regex_pattern2 = r"Type: [a-zA-Z]\w+"
                  regex_pattern3 = r"Type:\s[0-9]\+ \w+"

                  job_title = re.findall(regex_pattern,newBody)
                  job_title = ":".join(job_title).split(":")
                  dict_num["Title"] = job_title[1]

                  emp_type = re.findall(regex_pattern2, newBody)
                  emp_type2 = re.findall(regex_pattern3, newBody)
                  job_type = emp_type + emp_type2
                  job_type = ":".join(job_type)
                  job_type = job_type.split(":")
                  dict_num["EmploymentType"] = job_type[1]
                  b1,b2,b3 = newBody.partition('Description')
                  NewDescription = b3.replace(" 0.", "").replace("-0.", "").replace(":  ", "")
                  dict_num['JobDescription'] = NewDescription

      data_list.append(dict_num)

rv, data = M.select("\"INBOX\"")
if rv == 'OK':
    process_mailbox(M)
    M.close()
M.logout()
### End of Gmail

### If the list is empty do nothing but a message.
if not data_list:
    print("The Inbox has no new emails")
else:
    ## creating Dataframe
    df = sc.parallelize(data_list)\
        .map(lambda x: json.dumps(x))

    myDatas = spark.read.json(df)

    ## Call the function toSQL
    toSQL(myDatas)
