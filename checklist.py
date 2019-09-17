checklist = []
def create(item): #create
    checklist.append(item)

def read(index): #index
    return checklist[index]

def update(index, item): #update
    checklist[index] = item

def destroy(index): #destroy
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + " " + list_item)
        index += 1
def user_input(prompt):
    user_input = input(prompt)
    return user_input
def mark_completed(index):
    for i in range(len(checklist)):
        if index == i:
            print(update(index,"√"+str(read(index))))

def unmarked(index):
    for i in range(len(checklist)):
        if index == i:
            string = read(index)
            if string[0] == "√":
                replacement = string.replace("√", "")
                update (index, replacement)
def checkIndex(index):
    if (index < len(checklist) and index >= 0):
        return True
    else:
        print("Please fix index error")

def select(function_code):
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)


    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "M" or function_code == "m":
        list_all_items()
        marked = int(user_input("Index to mark complete is: "))
        if checkIndex(marked) == True:
            mark_completed(marked)
            list_all_items()

    elif function_code == "N" or function_code == "n":
        list_all_items()
        unmark = int(user_input("Index to unmark is: "))
        if checkIndex(unmark) == True:
            unmarked(unmark)
            list_all_items()

    elif function_code == "U" or function_code == "u":
        list_all_items()
        index = int(user_input("Index to update is: "))
        if checkIndex(index) == True:
            item = user_input("Input new Item: ")
            update(index, item)
            list_all_items()

    elif function_code == "Q" or function_code == "q":
        return False

    elif function_code == "R" or function_code == "r":
        index = int(user_input("Index to remove is "))
        if checkIndex(index) == True:
            destroy(index)
            list_all_items()

    else:
        print("Unknown Option")
    return True

#def test():
#    create("purple sox")
#    create("red cloak")
#    update(0, "purple socks")
#    destroy(1)
#test()
#user_value = user_input("Please Enter a value:")
#print(user_value)

running = True
while running:
    selection = user_input("""Press C to add to list, R to Remove from list,
P to display list, U to update, M to mark as complete,
N to Unmark, and Q to quit. """)
    running = select(selection)
