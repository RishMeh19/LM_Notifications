
Running instructions:
In python console:
    from main import *
Use all the functions as mentioned in Question statement
Eg:
    addUser('A', '1A', 'admin') : userName, userId, role. P.S: userId not mention in Question statement, but should be there to uniquely identify the user
    addTopic('A', 'Fun')
    subscribeTopic('A', 'Func')
    viewSubscribedTopics('A')
    postEvent(messageBody): messageBody = {'id':'F', 'topicName':'Poke', 'Text':'invite'}
    removeUser('B', 'A')
    removeTopic('F', 'A')

run(): to implement queue processing and broadcasting message, will run as a background thread, output in output.txt file 