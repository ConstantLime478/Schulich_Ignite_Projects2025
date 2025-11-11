class Eevee:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def growl(self):
        print(f"{self.name} used Growl!")
        
    def tackle(self):
        print(f"{self.name} used Tackle!")
        
        
class Jolteon(Eevee):
    def __init__(self, name, type):
        super().__init__(name, type)      
        
    def thunder(self):
        print(f"{self.name} used Thunder!")
        
        
jolteon = Jolteon("jolteon", "Electric")
jolteon.growl()
jolteon.tackle()
jolteon.thunder()

    