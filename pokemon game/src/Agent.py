
class Agent:
    def __init__(self, id: int, value: float, src: int, dest: int, speed: float, pos: ()) -> None:
        self.id: int = id
        self.value: float = value
        self.src: int = src
        self.dest: int = dest
        self.speed: float = speed
        self.pos: () = pos
        self.pokeball = False

    def setDest(self, dest: int):
        self.dest = dest

    def __repr__(self):
        return "Agent:" + " id:" + self.id.__repr__() + ",value" + self.value.__repr__() + ",src" + self.src.__repr__() + ",dest" + self.dest.__repr__() + ",speed" + self.speed.__repr__() + ",pos" + self.pos.__repr__()
