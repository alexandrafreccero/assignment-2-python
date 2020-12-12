class Scene:
    def __init__(self, path):           
        the_file = open(path, 'r')      
        
        text = []                       
        options = []                    
        for line in the_file.readlines(): 
            if '%' in line:             
                line = line.split('%')  
                line_as_dictionary = {  
                    "question":line[0], 
                    "file":line[1].strip()      
                }
                options.append(line_as_dictionary)  
            elif not "%" in line:                   
                text.append(line)               

        self.scene_to_print = text       
        self.options = options           
        self.path = path                


    def play(self):                       
        
        for line in self.scene_to_print:
            print(line)

        valid_answer = False  
        while not valid_answer:
            counter = 1                     
            for choice in self.options:      
                print(counter, choice["question"]) 
                counter = counter + 1              
            
            try:
                answer = input("> ")             

                
                if answer == "q" or self.path == 'exit.txt' or len(self.options)==0:       
                    print("thank you for playing, have a nice day!") 
                    exit()  
                        
                answer = int(answer)       
                valid_answer = 1 <= answer <= len(self.options)
                if not valid_answer:
                    print("You did not enter a correct number, please try again.")
            except ValueError: 
                print("Something went wrong, please retry")
                
        
        choosen_option = self.options[answer-1]
        
        next_scene = Scene(path=choosen_option["file"]) 
        next_scene.play()

the_scene = Scene(path='intro.txt')
the_scene.play()
