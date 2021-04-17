
import random
all_characters = []
current_characters = []#random.sample(all_characters, 2)

def main():
    global all_characters, current_characters
    all_characters = [RedRidingHood(), Grandmother(), Hunter(), Wolf(), FairyGodMother()]
    random.shuffle(all_characters)
    current_characters = [all_characters.pop(), all_characters.pop()]
    
    
    running = True
    num_reacted = 0
    while running:
        anyReacted = False
        str = 'Current Characters: '
        for c in current_characters:
            str += c.name + " "
        print(str)
        print('')
        for c in current_characters:
            if not isinstance(c, FairyGodMother):
                temp_char_list = c.react(current_characters, num_reacted)
                if c.reacted:
                    anyReacted = True
                    print(c.reactedText)
                    print('')
                    current_characters = temp_char_list
                    break
        num_reacted += 1
        
        if not anyReacted:
            if any(isinstance(item, FairyGodMother) for item in all_characters):
                for c in all_characters:
                    if isinstance(c, FairyGodMother):
                        current_characters.append(c)
                        current_characters = c.react(current_characters, num_reacted)
                        print(c.reactedText)
                        running = False
                        break
            elif any(isinstance(item, FairyGodMother) for item in current_characters):
                for c in current_characters:
                    if isinstance(c, FairyGodMother):
                        current_characters = c.react(current_characters, num_reacted)
                        print(c.reactedText)
                        running = False
                        break
        

class RedRidingHood():
    global all_characters
    name = "Red Riding Hood"
    reacted = False
    reactedText = ''
    def __init__(self):
        pass
    
    def react(self, char_list, num_reactions):
        index = char_list.index(self)
        self.reacted = True
        if any(isinstance(item, Grandmother) for item in char_list) and len(char_list) == 2:
            self.reactedText = self.name + " and Grandmother eat some pie."
            for c in all_characters:
                if isinstance(c, FairyGodMother):
                    char_list.append(all_characters.pop(all_characters.index(c)))
                    self.reactedText += "\nAnd the Fairy God Mother appears!"
            
        elif any(isinstance(item, Hunter) for item in char_list) and len(char_list) == 2:
            self.reactedText = self.name + " starts screaming! "
            for c in all_characters:
                if isinstance(c, Grandmother):
                    char_list.append(all_characters.pop(all_characters.index(c)))
                    self.reactedText += "\nSo the Grandmother appears!"

        elif any(isinstance(item, Wolf) for item in char_list)  and any(isinstance(item, FairyGodMother) for item in all_characters):
            for c in all_characters:
                if isinstance(c, FairyGodMother):
                    self.reactedText = self.name + " gives th Wolf flowers. \nThe Wolf starts to cry from happiness"
                    char_list.append(all_characters.pop(all_characters.index(c)))

        elif not any(isinstance(item, Wolf) for item in char_list) and num_reactions >= 3:
            self.reacted = False
            for c in all_characters:
                if isinstance(c, Wolf):
                    self.reacted = True
                    self.reactedText = self.name + " turns into the Wolf!!!"
                    char_list[index] = all_characters.pop(all_characters.index(c))
        else:
            self.reacted = False
        return char_list

class FairyGodMother():
    global all_characters
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

class Grandmother():
    global all_characters
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
        elif not any(isinstance(item, RedRidingHood) for item in char_list) and any(isinstance(item, Hunter) for item in char_list) and any(isinstance(item, FairyGodMother) for item in all_characters):
            self.reactedText = self.name + " and the Hunter eat a piece of pie. "
            for c in all_characters:
                if isinstance(c, FairyGodMother):
                    char_list.append(all_characters.pop(all_characters.index(c)))
                    self.reactedText += "\nAnd the Fairy God Mother appears!"
        elif any(isinstance(item, Wolf) for item in char_list):
            self.reactedText = self.name + " kills the wolf!"
            for c in char_list:
                if isinstance(c, Wolf):
                    char_list.pop(char_list.index(c))
                    break
        elif not any(isinstance(item, RedRidingHood) for item in char_list) and any(isinstance(item, FairyGodMother) for item in char_list) and any(isinstance(item, RedRidingHood) for item in all_characters):
            self.reactedText = self.name + " wishes to be with Red Riding Hood."
            for c in all_characters:
                if isinstance(c, RedRidingHood):
                    char_list.append(all_characters.pop(all_characters.index(c)))
                    self.reactedText += "\nThe Fairy God Mother fulfills the wish and Red Riding Hood appears!"
        elif len(char_list) == 1 and any(isinstance(item, Hunter) for item in all_characters):
            self.reactedText = self.name + " bakes a pie! "
            for c in all_characters:
                if isinstance(c, Hunter):
                    char_list.append(all_characters.pop(all_characters.index(c)))
                    self.reactedText += "\nThe Hunter can smell the pie and shows up!"
        else:
            self.reacted = False
        return char_list

class Wolf():
    global all_characters
    name = "The Wolf"
    reacted = False
    reactedText = ''
    def __init__(self):
        pass
    
    def react(self, char_list, num_reactions):
        index = char_list.index(self)
        self.reacted = True
        if not any(isinstance(item, RedRidingHood) for item in char_list) and any(isinstance(item, FairyGodMother) for item in char_list):
            self.reactedText = self.name + " wishes to eat a child! \nThe Fairy God Mother gets angry and slays the Wolf!"
            for c in char_list:
                if isinstance(c, Wolf):
                    char_list.pop(char_list.index(c))
                    break
        else:
            self.reacted = False
        return char_list

class Hunter():
    global all_characters
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
            for c in char_list:
                if isinstance(c, Wolf):
                    char_list.pop(char_list.index(c))
                    break
        else:
            self.reacted = False
        return char_list



main()