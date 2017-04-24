from dish import Dish #first is docname second classname

class Menu: 
    def __init__(self): #this is the constuctor
        self.menu = [] #creates a variable (array) called menu
        
        self.menu.append(Dish(dish_name="Margherita"))
        self.menu.append(Dish(dish_name="Napoletana"))
        self.menu.append(Dish(dish_name="Pepperoni"))
    
    def contents(self):
        return self.menu
    

    
    #instance of a class? en  wanneer draait die ? 
    
    #wat is constructer?
    
    #argument? 
    
    #object 
        #instance van een class
    
    #class 
        #blueprint for object
