import sys

contacts = []
def add_contact(name: str, num: int)->str:
    for contact in contacts:
        if contact["number"] == num:
            return f"Contact with phone [{contact['number']}] already exists ( {contact['name']} )"

        if contact["name"] == name:
            return f"Contact [{contact['name']}] already exists ({contact['number']} )"

    contacts.append({"name": name, "number": num})
    return f"Contact [{name}] added successfully with number:{num} "

def change_contact(name: str, num: int) -> str:
    for contact in contacts:
        if contact["name"] == name:
            contact["number"] = num
            return f"Number if contact [{contact['name']}] changed to {contact['number']} "

    return f"Contact [{name}] does not exist"

def show_phone(name:str) -> str:
    for contact in contacts:
        if contact["name"] == name:
            return f"[{name}] number is {contact["number"]}"

    return f"Contact [{name}] does not exist"

def show_all():
    text = "---name----|---number---\n"
    for contact in contacts:
        t = f"{contact["name"]}   :   {contact["number"]}\n"
        text = text + t
    return text

def run_command(p:str,args:list[str]) -> str:
    if not args:
        return "Arguments wasn't find"

    if p == "add" and len(args) > 1 and args[1].isdigit():
        return add_contact(args[0], int(args[1]))
    elif p == "change" and len(args) > 1 and args[1].isdigit():
        return change_contact(args[0], int(args[1]))
    elif p == "phone":
        return show_phone(args[0])
    else:
        return "Wrong arguments of command"


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
                print(run_command(p, args))
        elif p == "all":
            print(show_all())
        else:
            print("Invalid command")



if __name__ == "__main__":
    main()
