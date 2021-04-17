from characters.Wolf import Wolf


class Hunter():
    name = "The Hunter"
    reacted = False
    reactedText = ''
    def __init__(self):
        pass
    
    def react(self, char_list, num_reactions):
        index = char_list.index(self)
        self.reacted = True
        if any(isinstance(item, Wolf) for item in char_list):
            self.reactedText = self.name + " shoots the Wolf"
            char_list.pop(index)
        else:
            self.reacted = False
        
        