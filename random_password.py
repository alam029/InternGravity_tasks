import random



# Define character pools

uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

lowercase = list("abcdefghijklmnopqrstuvwxyz")

digits = list("0123456789")

symbols = list("~!@#$%^&*(){}|-/?><")



# Function to build the password character pool

def list_passwords():

    try:

        include_cha = input("Include Letters (y/n): ").lower()

        include_dig = input("Include Digits (y/n): ").lower()

        include_sym = input("Include Symbols (y/n): ").lower()



        password_list = []

        required_chars = []



        if include_cha == "y":

            password_list += uppercase + lowercase

            required_chars.append(random.choice(uppercase)) #include at least one uppercase letter

        else:

            return None, "Enter only (y/n) in avery choise"



        if include_dig == "y":

            password_list += digits

            required_chars.append(random.choice(digits))

        else:

            return None, "Enter only (y/n) in avery choise"



        if include_sym == "y":

            password_list += symbols

            required_chars.append(random.choice(symbols))

        else:

            return None, "Enter only (y/n) in avery choise"



        if not password_list:

            return None, "Password not generated. You must include at least one character type."



        return password_list, required_chars



    except Exception as e:

        return None, f"Error : {e}"



#function to generate a random password

def random_password(ln_password, password_list, required_chars):

    if ln_password < len(required_chars):

        return None, f"Password length must be at least {len(required_chars)} to include all selected types."



    remaining_length = ln_password - len(required_chars)

    password = required_chars + [random.choice(password_list) for _ in range(remaining_length)]



    random.shuffle(password)

    return ''.join(password), None



#main program

try:

    ln_password = int(input("Enter your desired password length: "))

    password_list, required_chars_or_msg = list_passwords()



    if password_list:

        password, error = random_password(ln_password, password_list, required_chars_or_msg)

        if password:

            print(f"\nGenerated Password: {password}")

        else:

            print(error)

    else:

        print(required_chars_or_msg)



except ValueError:

    print("Please enter a valid number for password length.")