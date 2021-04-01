from time import sleep
from User import User

procQ = []
userDict = {}
topicDict = {}

def addUser(userName, uid, role):
    if userDict.get(userName):
        print ('User already present')
    else:
        try:
            userDict[userName] = User(userName, uid, role)
            print ('success')
        except:
            print ('try again')


def addTopic(userName, topicName):
    if topicDict.get(topicName):
        print ('Topic already Present')
    else:
        if userDict.get(userName):
            user = userDict[userName]
            print (user.addTopic(topicName, topicDict))
        else:
            print ('User not present')


def subscribeTopic(userName, topicName):
    if userDict.get(userName):
        if topicDict.get(topicName):
            try:
                topic = topicDict[topicName]
                topic.addUser(userName)
                user = userDict[userName]
                user.subscribeTopic(topicName)
                print ('User subscribed successfully')
            except:
                print ('Try again')
        else:
            print('Topic with given name not present')
    else:
        print ('User with given name not present')


def viewSubscribedTopics(userName):
    if userDict.get(userName):
        try:
            user = userDict[userName]
            topics = user.getSubscibedTopics()
            print ('Subscribed Topics are: ')
            for t in topics:
                print (t)
        except:
            print ('Try again')
    else:
        print('User not found')


def postEvent(messageBody):
    topicName = messageBody['id']
    if topicDict.get(topicName):
        try:
            topic = topicDict[topicName]
            topic.addEvent(messageBody['topicName'], messageBody['Text'], procQ)
            print ('Event added successfully')
        except:
            print ('Try again')
    else:
        print ('Topic not present')


def removeUser(userName1, userName2):
    if userName1 == userName2:
        print ('Cannot remove self')
    else:
        if userDict.get(userName2):
            try:
                u2 = userDict[userName2]
                print(u2.removeUser(userName1, userDict))
                #print ('User removed successfully')
            except: 
                print ('Try again')
        else:
            print('User not found')


def removeTopic(userName, topicName):
    if userDict.get(userName):
        try:
            u = userDict[userName]
            print (u.removeTopic(topicName, topicDict))
        except: 
            print ('Try again')
    else:
        print('User not found')

def script():
    while True:
        if procQ:
            file1 = open('output.txt', 'w+')
            while procQ:
                to = procQ.pop(0)
                for user in to.users:
                    file1.write(user + ' ' + to.evName + '\n')
                    file1.write(to.msg)
                    '''
                    print (user + ' ' + to.evName)
                    print (to.msg)
                    '''
            file1.close()
        sleep(5000)

import threading
def run():
    script_thread = threading.Thread(target=script, name="QProcessor")
    script_thread.start()
    