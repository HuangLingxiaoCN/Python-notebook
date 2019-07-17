# Notebook program

import time

f = "notebook.txt"

try:
    open(f,"r")
except IOError:
    print("No default notebook was found, created one.")



while True:
    print("Now using file ",f)
    print("""(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit
""")
	
	
	
    select = input("Please select one: ")
    if select == "1":
        # Read the content of the notebook
        file = open(f,"r")
        print(file.read())
        file.close()
		
		
    elif select == "2":
        # Append a new note to the notebook
        file = open(f,"a")
        mes = input("Write a new note: ")
        file.write(mes+":::"+time.strftime("%X %x")+"\n")
        file.close()
		
		
    elif select == "3":
        # Empty notebook
        file = open(f,"w")
        # file.write("")
        print("Notes deleted.")
        file.close()
		
		
    elif select == "4":
        f = input("Give the name of the new file: ")
        try:
            open(f,"r")
        except:
            print("No notebook with that name detected, created one.")
            open(f,"x")
            		
    elif select == "5":
        # Quit
        print("Notebook shutting down, thank you.")
        break

		
