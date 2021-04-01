from Topic import Topic

class User:
    def __init__(self, name, uid, role):
        self.name = name 
        self.id = uid
        self.subscribedTopics = set()
        self.role = role

    def subscribeTopic(self, topicName):
        self.subscribedTopics.add(topicName)

    def unsubscribeTopic(self, topicName):
        self.subscribedTopics.remove(topicName)
    
    def getSubscibedTopics(self):
        return self.subscribedTopics

    def addTopic(self, topicName, topicDict):
        if self.role != 'admin':
            return 'User not permissable to add Topics'
        try:
            topicDict[topicName] = Topic(topicName)
            return 'Topic added successfully'
        except:
            return 'Try Again'
    
    def removeUser(self, userName, userDict):
        if self.role != 'admin':
            return 'Not permissable to remove user'
        else:
            if userDict.get(userName):
                try:
                    u = userDict[userName]
                    del userDict[userName]
                    return ('User removed successfully')
                except: 
                    return('Try again')
            else:
                return('User not found')
    
    def removeTopic(self, topicName, topicDict):
        if self.role != 'admin':
            return 'Not permissable to remove topic'
        else:
            if topicDict.get(topicName):
                try:
                    t = topicDict[topicName]
                    del topicDict[topicName]
                    return ('Topic removed successfully')
                except: 
                    return ('Try again')
            else:
                return('Topic not found')   
