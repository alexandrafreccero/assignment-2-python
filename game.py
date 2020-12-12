class Scene:
    def __init__(self, path):           # initierar objectens egenskaper i klassen Scene
        the_file = open(path, 'r')      # Variablen the_file är en öppnad fil som kan läsas
        
        text = []                       #Skapar variabeln text, tom lista
        options = []                    #skapar variabeln options, tom lista
        for line in the_file.readlines(): # för varje rad i the_file. readlines, läses alla rader.
            if '%' in line:             # se efter om % finns i rad
                line = line.split('%')  # En rad blir delad vid % och kallas då line
                line_as_dictionary = {  # Dessa delade nya lines sätts in i en dictionary
                    "question":line[0], # Där första delen av delade raden, kallas question
                    "file":line[1].strip()      #och andra delen kallas file, tar bort allt utom text
                }
                options.append(line_as_dictionary)  # lägg till dictionaryn till options 
            elif not "%" in line:                   # Om inte % finns på raden -
                text.append(line)                   #lägg till raden i text variablen

        self.scene_to_print = text       # I Text har filens innehåll sparats som ska printas i aktuell scen
        self.options = options           # options har lista med dictionary,self.options sparar detta



    def play(self):                      # Funktion för själva spelets utförande
        for line in self.scene_to_print:
            print(line)
        
        counter = 1                      # Counter har värdet 1
        for choice in self.options:      #för varje val i lista
            print(counter, choice["question"]) #skriv ut siffra 1 och choice(val i lista)före % question
            counter = counter + 1              # för varje loop i lista lägg till ett
        

        answer = input()                 # answer är användarens val
        if len (self.options)==0:
            next_scene = Scene(path = "exit.txt") 
            next_scene.play()
        if answer == "q":                # Om använadren skriver q
            print("thank you for playing, have a nice day!") #Printas detta
            exit()                                           # spel avslutas
                
        answer = int(answer)            # gör om input till en int

        #använd answer för att välja korrekt option
        choosen_option = self.options[answer-1]
        #print (choosen_option['file'])
        next_scene = Scene(path=choosen_option["file"]) 
        next_scene.play()# använd 




# här körs spelet
the_scene = Scene(path='intro.txt')
the_scene.play()
