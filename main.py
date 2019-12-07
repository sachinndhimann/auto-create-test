#Author:Sachin Dhiman
#Date:07-12-2019


from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import json
import testingutil


trainingdata=[]
with open('test_utterances.json') as json_file:
    data = json.load(json_file)
key_list = list(data.keys()) 
val_list = list(data.values())  


for key,value in zip(key_list,val_list):
    result=(key,value)
    trainingdata.append(result)
	

tc=[]
testcasename=""
inputtestcase='TestCase01.txt'


with open(inputtestcase) as test_case:
    firstline = test_case.readline()
    testcasename=firstline
    line = test_case.readline()
    while line:
       
       line = test_case.readline()
       tc.append(line)
       

cl = NaiveBayesClassifier(trainingdata)
list_of_actions=[]

for testline in tc:
    print(testline)
    output=cl.classify(testline)
    print(output)
    if output is not "0":
        list_of_actions.append(output)	
	

print(testcasename)
#create_robot_file(testcasename)
#add_actions_to_robot_file(tc,list_of_actions)
#save_robot_file(testcasename)



