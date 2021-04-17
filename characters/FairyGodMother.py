class FairyGodMother():
    name = "Fairy God Mother"
    reacted = False
    reactedText = ''
    def __init__(self):
        pass
    
    def react(self, char_list, num_reactions):
        index = char_list.index(self)
        self.reacted = True
        self.reactedText = self.name + " makes everyone dissapear and the story ends!"
        return [char_list[index]]
        