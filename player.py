
class Player(object):

    def __init__(self,id,position):
        self.state = True
        self.id = id
        self.position = position
    def __str__(self):
        return "o"
