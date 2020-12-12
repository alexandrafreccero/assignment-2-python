class boll:
    def __init__(self,difference):
        self.lenght = 0
        self.difference = difference
        
        
    def sparka(self):
        self.lenght += self.difference
        if self.lenght >10:
            print(" Gold star")

        else:
            print("bronze star")
    
        

min_boll = boll(10)
min_boll.sparka()
min_boll.sparka()
print(min_boll.lenght)

trasig_boll = boll(5)
trasig_boll.sparka()
trasig_boll.sparka()
print(trasig_boll.lenght)
