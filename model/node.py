

class Node:
    
    def __init__(self, name, desc, action):
        self.name = name
        self.desc = desc
        self.action = action
        self.child = None
    
    def execute_action(self):
        self.action.execute(self)
        if self.child != None:
            self.child.execute_action()
            
