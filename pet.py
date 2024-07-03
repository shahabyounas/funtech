class Pet: 
    
    # Constructor initial/default state of the Pet
    def __init__(self, name):
         self.name = name
         self.health = 100
         self.hunger = 0
         self.happiness = 100
         
    # Reduces hunger and can improve health slightly.
    # The pet eat 100 units of food
    def eat(self, amount):
        self.hunger = self.hunger - amount
        if self.hunger < 0:
            self.hunger = 0  #Not Hungry
        
        self.health = self.health + amount
        if self.health > 100:
            self.health = 100
            
        
    # Increases happiness and can affect health.
    # Our pet can play for 100 mins and each minute playing is accounted for a unit of happiness and health
    def play(self,time):
        self.happiness = self.happiness + time
        if self.happiness > 100:
            self.happiness = 100 # very happy
        
        self.health = self.health - time
        if self.health < 0:
            self.health = 0 #Very unhealthy

    
    # Improves health but may affect happiness.
    # Each time a pet take medicine the health increases by 50 units and happiness decreases by 50 units
    def give_medicine(self):
        self.health = self.health + 50
        if self.health > 100:
            self.health = 100
            
        self.happiness = self.happiness - 50
        if self.happiness < 0:
            self.happiness = 0
        
    
    # Displays the current status of the pet, including health, hunger, and happiness levels.
    def check_status(self):
        print('*************************')
        print(f'The current status of the {self.name}')
        print(f"the current happiness {self.happiness}, health {self.health} and hunger {self.hunger} levels")
        


class TestPet(Pet):
    def __init__(self, name):
        super().__init__(name)
        
    def testPet(self, task, quantity = 0):
        match task:
            case 'eat':
                self.eat(quantity)
            case 'play':
                self.play(quantity)
            case 'medicine':
                self.give_medicine()
            case 'status':
                self.check_status() 
            case _: 
                print('Please enter a valid task type')


if __name__ == "__main__":
    pet = TestPet('Tommy')
    
    while True:
        print('\n******************************\n')
        print('Please Enter the valid task')
        task = input()
        
        amount = 0
        if task in ['eat', 'play']:
            print('Enter the amount')
            amount = input()
        
            if not amount.isnumeric():
                print('Please enter valid number')
                continue
            amount = int(amount)
            
        
        pet.testPet(task, amount)

