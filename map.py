from empty import Empty
from wall import Wall


class Map(object):

    def __init__(self, size):

        self.grid = []
        for i in range(size):

            if i%(size-1) == 0:
                line = [Wall()]*size
            else:
                line = [Empty()]*size
                line[0] = Wall()
                line[size-1] = Wall()
            self.grid.append(line)
