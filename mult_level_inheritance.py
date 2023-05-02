class MoveCharacter:
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")


class JumpCharacter(MoveCharacter):
    def jump1levelup(self):
        print("Jump 1 level up")

    def jump2levelup(self):
        print("Jump 2 level up")


class Pokemon(JumpCharacter):
    pass


p = Pokemon()

p.move_bwd()
p.jump1levelup()

class Mickey(JumpCharacter):
    pass

m = Mickey()
m.move_fwd()

''' Method resolution order - > mro() -
Current class->  Search first in the current class and then Parent class Depth First lef tot right fashion'''

print(Pokemon.mro())