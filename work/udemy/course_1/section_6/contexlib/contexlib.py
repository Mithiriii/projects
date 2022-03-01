class Door:

    def __init__(self, where):
        self.where = where

    def open(self):
        print("Opening door to the {}".format(self.where))

    def close(self):
        print("Closing door to the {}".format(self.where))


door1 = Door('hell')
door2 = Door('future')

door1.open()
door1.close()
door2.open()
door2.close()