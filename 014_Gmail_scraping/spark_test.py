from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark.sql import SparkSession
import json
from json import loads
import pprint

import sys
import imaplib
import getpass
import email
import re
from collections import namedtuple

# --packages mysql:mysql-connector-java:5.1.39

sc = SparkContext(appName="GmailToMySQL")
spark = SparkSession(sc)

# fields = ("Date","Employment", "From", "JobDescription", "Message", "PhoneNumber", "Title" )
# MyGmails = namedtuple( 'myEmail', fields )

data_list = []

def toSQL(df):
    df.show()
    # df.write.format("jdbc")\
	# .mode("overwrite")\
	# .option("url", "jdbc:mysql://localhost:3306/hadoop_test") \
	# .option("dbtable", "gmail_table") \
	# .option("user", "sqoop_user") \
	# .option("password", "Welcome2BB") \
	# .option("driver", "com.mysql.jdbc.Driver") \
	# .save()

# def savetheresult( rdd ):
#     if not rdd.isEmpty():
#     	df = spark.createDataFrame(rdd)
#     	toSQL(df)

### Read Emails from Gmail Account

M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    # M.login('enhanceit.test@gmail.com', getpass.getpass())
    M.login('enhanceit.test@gmail.com', "Welcome2BB")
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")
rv, mailboxes = M.list()
# if rv == 'OK':
#     print("Mailboxes:")
#     print(mailboxes)
def process_mailbox(M):
  rv, data = M.search(None, "ALL") #"ALL" has to be switch with UNSEEN in order to see the json if it's working b/c it won't work after you run it the first time
  if rv != 'OK':
      print("No messages found!")
      return
#   data_list = []
  for num in data[0].split():
      rv, data = M.fetch(num, '(RFC822)')
      if rv != 'OK':
          print("ERROR getting message", num)
          return
      dict_num = {}
      msg = email.message_from_string(data[0][1].decode('utf-8'))
    #   dict_num['From'] = msg['From'].replace(" <", ", <").split(",")
      dict_num['From'] = msg['From']
      subject = msg['Subject']
      mess = subject.replace("Fwd: ", "")
      dict_num["Message"] = mess
      dict_num['Date'] = msg['Date']
      #print(dict_num)

      if msg.is_multipart():
          # iterate over email parts
          for part in msg.walk():
              # extract content type of email
              content_type = part.get_content_type()
            #   content_disposition = str(part.get_content_disposition())
              content_disposition = str(part.get('content disposition'))
            #   try:
            #       # get the email body
            #       body = part.get_payload(decode=True).decode()
            #   except:
            #       pass
              if content_type == "text/plain" and "attachment" not in content_disposition:
                  body = part.get_payload().decode()
                  # print text/plain emails and skip attachments
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
                  jobList1 = re.compile('(\s[\d]+\.)(.*?)(?=(\s[\d]+\.))',re.DOTALL)
                #   jobList1 = re.compile('(\s[\d])(.*?)(?=(\s[\d]))',re.DOTALL)
                #   dict_num['JobDescription'] = re.findall(jobList1, b3)
                  JobDescriptionList = re.findall(jobList1, b3)
                  dict_num['JobDescription'] = ""

                  for jobs in JobDescriptionList:
                      for jobsTupple in jobs:
                          newTupple = re.sub("(\s\d\.,)(.*?)(?=(\s\d\.,))", "", jobsTupple)
                          dict_num['JobDescription'] += newTupple


                #   for jobs in JobDescriptionList:
                #       for jobsTupple in jobs:
                #           for x in jobsTupple:
                #               dict_num['JobDescription'] += x + ", "


                  # print(dict_num)
      data_list.append(dict_num)
#   pprint.pprint(data_list, indent=4)


rv, data = M.select("\"INBOX\"")
if rv == 'OK':
    # print("Processing mailbox...\n")
    process_mailbox(M)
    M.close()
M.logout()
### End of Gmail

# print(myDatasMails)
# .map(lambda x: json.loads(x[1])).flatMap(lambda x: x['data'])

df = sc.parallelize(data_list)\
    .map(lambda x: json.dumps(x))

myDatas = spark.read.json(df)

toSQL(myDatas)

# myDatas.show()


# print(df)



    # .map(lambda x: json.dumps(x))\
    # .map(lambda s: s)\
    # .collect()
    # .map(lambda x: MyGmails(x['Date:'], x['Employment Type'], x['From'], x['Job Description'], x['Message'], x['Phone Number'], x['Title'] ))\
    # .collect()

# print(df)

# myDatas = spark.read.json(df)

# df.show()


# df = spark.createDataFrame(rdd)



# myDatas.show()

# myDatas = spark.read.json(data_list)

# print(myDatas)

# rdd = sc.parallelize(data_list).collect()

# for x in rdd:
#     # savetheresult(mails)
#     test = MyGmails(x['Date:'], x['Employment Type'], x['From'], x['Job Description'], x['Message'], x['Phone Number'], x['Title'] )
#     # print(test)
#     savetheresult(x)

# print(rdd)

# hasattr(rdd, "toDF")
## True
# rdd.toDF().show()
# eee = rdd.map(lambda x: x).foreachRDD(lambda x: savetheresult(x))

# print(eee)

# result = firstRDD.flatMap(lambda x: x)

# print(firstRDD)

# print(type(firstRDD))



# print(data_list)

# myEmailData = data_list.map(lambda x: x)
# result = flatMap(lambda x: x, data_list)

# print(myEmailData)
# print(result)
# print(data_list)



    # .map(lambda x: myEmail(x['Date'], x['Employment'], x['From'], x['Job Description'], x['Message'], x['Phone Number'], x['Title'] ))\
    # .foreachRDD(lambda x: savetheresult(x))
