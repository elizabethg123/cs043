import database

while True:
    type = input("type: ")
    if type=="a":
        name = input("name: ")
        number = input("number: ")
        database.insert('directory.txt', name, number)
    if type=="f":
        name = input("name: ")
        found = str(database.select_one('directory.txt', name))
        if found == "None":
            print("Name not in directory")
        else:
            print(found)
    if type=="d":
        name = input("name: ")
        found = str(database.select_one('directory.txt', name))
        if found == "None":
            print("Name not in directory")
        else:
            database.delete('directory.txt', name)
    if type=="u":
        name = input("name: ")
        found = str(database.select_one('directory.txt', name))
        if found == "None":
            print("Name not in directory")
        else:
            number = input("new number: ")
            database.update('directory.txt', name, number)
    if type=="q":
        break
    
            
    
        

    

