from waiter import Waiter
from menu import Menu

pietje = Menu()
#this makes an instance of menue which makes 3 instances of dish hierachy : 
# menu 
    #menukakaart 
        #dish 1
            #name
        #dish 2
            #name
        #dish 3
            #name

#hier maak je instance aan van de waiter die in de constructor 
#een argument menu heeft en menu moet gelijk worden aan het object menu wat ik hier pietje heb genoemd
# dus menu word pietje 
w = Waiter(menu=pietje)

w.greet_guest()
w.serve_guest()

  
    #instance of a class? 
        #een copie van de klasse
    #wat is constructer?
        #is executed when an instance is created
    #argument? 
        #is an variable of an object (instance of a class)
    #object 
        #instance van een class
    #class 
        #blueprint for object
    #methods 
        #functions of a class
        
        
