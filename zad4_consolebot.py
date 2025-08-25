import sys

contacts = []
def add_contact(name: str, num: int):
    for contact in contacts:
        if contact["number"] == num:
            print(f"Contact with phone {contact['number']} already exists ( {contact['name']} )")
            return
        if contact["name"] == name:
            print(f"Contact with name {contact['name']} already exists ({contact['number']} )")
            return
    contacts.append({"name": name, "number": num})
    print(f"Contact {name} added successfully with number:{num} ")



def change_contact(name: str, num: int):
    for contact in contacts:
        if contact["name"] == name:
            contact["number"] = num
            print(f"Contact {contact['name']} changed to {contact['number']} ")
            return
    print(f"Contact with name {name} does not exist")

def show_phone(name:str):
    for contact in contacts:
        if contact["name"] == name:
            print(f"{name}'s number is {contact["number"]}")
            return
    print(f"Contact with name {name} does not exist")

def show_all():
    print("---name----|---number---")
    for contact in contacts:
        print(contact["name"], contact["number"],sep="   :   ")


def run_command(p:str,args:list[str]):
    if len(args)>1 and not args[1].isdigit():
        print("Wrong number format")
        return
    if p == "add":
        add_contact(args[0], int(args[1]))
    elif p == "change":
        change_contact(args[0], int(args[1]))
    elif p == "phone":
        show_phone(args[0])


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        p, *args = user_input.split()
        p = p.strip().lower()
        if p == "exit" or p == "close":
            print("Goodbye")
            sys.exit()
        elif p == "hello":
            print("How can I help you?")
        elif p == "add" or p == "change" or p == "phone":
            if not args or len(args)<1 or len(args)<2 and (p == "add" or p == "change"):
                print("Wrong arguments")
            else:
                run_command(p, args)
        elif p == "all":
            show_all()
        else:
            print("Invalid command")




if __name__ == "__main__":
    main()












