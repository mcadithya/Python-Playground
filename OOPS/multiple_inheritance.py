class Italian():

    orgin:str

    def __init__(self,orgin):

        self.orgin=orgin

    def serving_pizza(self):

        print('serving pizza')

    def serving_pasta(self):

        print('serving pasta')

    def serving_steak(self):

        print('serving steak') 

class Chinese() :

    orgin:str

    def __init__(self,orgin):

        self.orgin=orgin

    def serving_sushi(self):

        print('serving sushi')

    def serving_dumplings(self) :

        print('serving dumpling chicken')   

class Arabic:

    orgin=str       

    def __init__(self,orgin):

        self.orgin=orgin

    def serving_mandi(self):

        print('serving mandi') 

    def serving_kunafa(self):
        
        print('serving kunafa')   



class Hotel (Italian,Chinese,Arabic):


    def __init__(self, orgin,name):

        Italian.__init__(self,orgin) 

        Chinese.__init__(self,orgin)

        Arabic.__init__(self,orgin)    

        self.name=name

        print(self.name)

garam_masala=Hotel('continental',' garammasala')     

garam_masala.serving_dumplings()

garam_masala.serving_kunafa()

garam_masala.serving_mandi()
        
print(Hotel)

        