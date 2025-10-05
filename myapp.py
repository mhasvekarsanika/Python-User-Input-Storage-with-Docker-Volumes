# Ask for user name
user_name = input("Enter your name to store in file or press Enter to proceed: ")

# If user entered a name, append it to file
if user_name:
    with open('user_info.txt', 'a') as file:
        file.write(user_name + "\n")

# Ask if they want to see stored names
show_info = input("Do you want to see all user names? y/n: ")

if show_info.lower() == 'y':
    try:
        with open('user_info.txt', 'r') as file:
            content = file.readlines()   # <-- fixed assignment
    except Exception as e:
        print(e, type(e))
    else:
        for line in content:
            print(f'{line.rstrip()}')
