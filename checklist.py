checklist = list()
def create(item): #create
    checklist.append(item)


def read(index): #read
    return checklist[index]

def update(index, item): #update
    checklist[index] = item

def destroy(index): #destroy
    checklist.pop(index)
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1
def user_input(prompt):
    user_input = input(prompt)
    return user_input
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    else:
        print("Unknown Option")
def test():
    create("purple sox")
    create("red cloak")

    #print(read(0))
    #print(read(1))

    update(0, "purple socks")
    destroy(1)

    #print(read(0))
    #print(read(1))
    #list_all_items()
    if select("C"):
        list_all_items()
    elif select("R"):
        list_all_items()
    elif select("P"):
        list_all_items()
    elif select("Q"):
        list_all_items()

test()
running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)
