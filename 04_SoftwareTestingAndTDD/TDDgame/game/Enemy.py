class Enemy():
    def __init__(self, name):
        self.name = name
        self.lives = 10

    def receive_dmg(self):
        self.lives = self.lives -1

    def is_alive(self):
        if self.lives > 0:
            return True
        else:
            return False
