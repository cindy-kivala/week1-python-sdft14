import ipdb

# print(type("Hello SDFT14!!!"))

my_name = "Mercy Nzau"


# print(my_name)

 #break code execution here, 



# // functionKeyword nameOfFunction(parameters if any){
# //     return Statement
# // }

# def funcName(is this function receiving any data?if yes, variables for all this data goes here):
    # all your operations
    # return (what do I Want the value of this function to be, whenever this function is called, what should it return?)


# invoke function using function name for it to run. Don't forget to pass all the data needed by the function, this data will be passed as arguments

def say_hi(greeted_person):
    # ipdb.set_trace()
    return f"I have been told to say Hi {greeted_person}!"

# print(say_hi("Kaynan"))


#virtual environment=> separate, isolated space/container that python creates where it installs all its packages and dependencies
# this means that to use these dependencies, we need to first be inside the space/container

# how are these containers created and how to get inside them => use virtual environment management tools, e.g pipenv 
# virtualenvironment tools, venv, virtualenv, pipenv, => help us create virtual environments, these separate containers, you cannot run two of these simultaneously

# pipenv shell => gets you inside the virtual environment, inside the isolated container

# Conditional Statements

# login UseCase: 
# users login with username, email and password
# if username, email and password are all correct, print("Login Successful, Welcome user, USERNAME")
# if username or email is correct and password is also correct, print("Login Successful, Welcome user, USERNAME")
#else, print("Login not successful")

username = "Mercy Nzau"
email = "mercy.nzau@moringaschool.com"
password = 1234

def login(username_input, email_input, password_input):
    
    if username_input == username and email_input == email and password_input == password:
        print(f"Login Successful, Welcome user, {username_input}")
    elif (username_input == username or email_input == email) and (int(password_input) == password): #False or True True
        # True and False // False
        # username and password correct or email and password correct
        print(f"Login Successful, Welcome user, {username_input}")
    else:
        print(f"Login UnSuccessful, Go Away you thief, {username_input}")
    # ipdb.set_trace()

entered_username = input("Enter your username:")
entered_email = input("Enter your Email")
entered_password = input("Enter your password")


login(entered_username, entered_email, entered_password)

# work out routine
workout_mapper = {"monday":"Leg Day", "Tuesday":"Core", "Wednesday":"Upper Arm", "Thursday":"Back", "Friday":"Cardio"}

# workout_oftheday = workout_mapper.get('monday')

def get_days_workout(weekday):
    return workout_mapper.get(weekday)

print(get_days_workout('Tuesday'))

for i in range(10):
    print(i)




























