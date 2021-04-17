from characters.Wolf import Wolf
from characters.Hunter import Hunter
from characters.FairyGodMother import FairyGodMother
from characters.Grandmother import Grandmother

class RedRidingHood():
    name = "Red Riding Hood"
    reacted = False
    reactedText = ''
    def __init__(self):
        pass
    
    def react(self, char_list, num_reactions):
        index = char_list.index(self)
        self.reacted = True
        if any(isinstance(item, Grandmother) for item in char_list) and len(char_list) == 2:
            self.reactedText = self.name + " and Grandmother eat some pie. \nAnd the Fairy God Mother appears!"
            char_list.append(FairyGodMother())
        elif any(isinstance(item, Hunter) for item in char_list) and len(char_list) == 2:
            self.reactedText = self.name + " starts screaming! \nSo the Grandmother appears!"
            char_list.append(Grandmother())
        elif any(isinstance(item, Wolf) for item in char_list):
            self.reactedText = self.name + " gives th Wolf flowers. \nThe Wolf starts to cry"
            char_list.append(Grandmother())
        elif not any(isinstance(item, Wolf) for item in char_list) and num_reactions >= 3:
            self.reactedText = self.name + " turns into the Wolf!!!"
            char_list[index] = Wolf()
        else:
            self.reacted = False
        return char_list
        
