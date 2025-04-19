
class Pet:
    def __init__(self, name):
        """Initialize a new pet with given name and default stats"""
        self.name = name
        self.hunger = 5  # Mid-range starting value
        self.energy = 5
        self.happiness = 5
        self.tricks = []  # For bonus feature
        
    def eat(self):
        """Reduce hunger and slightly increase happiness"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased!")
        
    def sleep(self):
        """Restore energy"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy increased!")
        
    def play(self):
        """Play with pet - affects multiple stats"""
        if self.energy >= 2:  # Need energy to play
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had fun playing!")
        else:
            print(f"{self.name} is too tired to play right now.")
    
    def get_status(self):
        """Print current pet stats"""
        print("\n" + "="*20)
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("="*20 + "\n")
        
    # Bonus methods
    def train(self, trick):
        """Teach pet a new trick"""
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}.")
    
    def show_tricks(self):
        """Display all learned tricks"""
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")