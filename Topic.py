
class Topic:
    def __init__(self, name):
        self.name = name 
        self.users = set()
        self.evName = ''
        self.msg = ''

    def addUser(self, uName):
        self.users.add(uName)
    
    def removeUser(self, uNmae):
        self.users.remove(uName)
    
    def addEvent(self, name, msg, q):
        self.evName = name 
        self.msg = msg
        q.append(self)