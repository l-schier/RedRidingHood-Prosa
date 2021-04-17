from characters.FairyGodMother import FairyGodMother


class Wolf():
    name = "The Wolf"
    reacted = False
    reactedText = ''
    def __init__(self):
        pass
    
    def react(self, char_list, num_reactions):
        index = char_list.index(self)
        self.reacted = True
        if any(isinstance(item, FairyGodMother) for item in char_list):
            self.reactedText = self.name + " wishes to eat a child! \nThe Fairy God Mother gets angry and slays the Wolf!"
            char_list.pop(index)
        else:
            self.reacted = False
        