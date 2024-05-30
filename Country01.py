def display_menu():
    print("Command Menu")
    print("view --> View country name")
    print("add --> Add a country")
    print("delete --> Delete a country")
    print("exit --> Exit the program")
    print()
    
def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_lines = "country codes: "
    for code in codes:
        codes_lines += code + " "
    print(codes_lines)
    
def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}. \n")
    else:
        print("There is no country with that code. /n")
        
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using that code ")
    else:
        name = input("Enter country code: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added. \n")

def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted")
    else:
        print("There is no country with that name. \n")
        
def main():
    countries = {"AF": "Afghanistan", "DE": "Germany", "US": "United States"}
    
    display_menu()
    while True:
        command = input("Command: ")
        command = code.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete(countries)
        elif command == "exit":
            print("Bye")
            break
        else:
            print("Not a valid command, please try again. \n")
            
if __name__ == "__main__":
    main()      

