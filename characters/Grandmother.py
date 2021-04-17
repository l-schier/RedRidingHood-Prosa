from characters.Wolf import Wolf
from characters.FairyGodMother import FairyGodMother
from characters.Hunter import Hunter
from characters.RedRidinghood import RedRidingHood


class Grandmother():
    name = "Grandmother"
    reacted = False
    reactedText = ''
    def __init__(self):
        pass
    
    def react(self, char_list, num_reactions):
        index = char_list.index(self)
        self.reacted = True
        if any(isinstance(item, RedRidingHood) for item in char_list) and any(isinstance(item, Hunter) for item in char_list):
            self.reactedText = self.name + " stabs the Hunter! (Stranger danger)"
            for c in char_list:
                if isinstance(c, Hunter):
                    char_list.pop(char_list.index(c))
                    break
        elif not any(isinstance(item, RedRidingHood) for item in char_list) and any(isinstance(item, Hunter) for item in char_list):
            self.reactedText = self.name + " and the Hunter eat a piece of pie. \nAnd the Fairy God Mother appears!"
            char_list.append(FairyGodMother())
        elif any(isinstance(item, Wolf) for item in char_list):
            self.reactedText = self.name + " kills the wolf!"
            for c in char_list:
                if isinstance(c, Wolf):
                    char_list.pop(char_list.index(c))
                    break
        elif any(isinstance(item, FairyGodMother) for item in char_list):
            self.reactedText = self.name + " wishes to be with Red Riding Hood. \nThe Fairy God Mother fulfills the wish and Red Riding Hood appears!"
            char_list.append(RedRidingHood())
        elif len(char_list) == 1:
            self.reactedText = self.name + " bakes a pie! \nThe Hunter can smell the pie and shows up!"
            char_list.append(Hunter())
        else:
            self.reacted = False
        return char_list
        