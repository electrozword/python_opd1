from dish import Dish #first is docname second classname

class Menu: 
    #this is the constructor of menu and will be executed when a instance of menu is made
    
    def __init__(self): #this is the constuctor
        #self.menu is an attributes who contains an array of objects (in this case objects of dishes)
        self.menukaart = [] 
        
        #in this part multiple things happen
        #1: the array .menu is filled with objects of dishes
        #2: when an instance of dish is made a name is given to the attribute who is given in the constructor
        
        self.menukaart.append(Dish(dish_name="chickensupremo"))
        self.menukaart.append(Dish(dish_name="Napoletana"))
        self.menukaart.append(Dish(dish_name="Pepperoni"))
    
    def contents(self):
        return self.menukaart
    

  
