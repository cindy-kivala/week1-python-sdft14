
def mydecorator(funcArg):
    # takes in a function as an argument(the function to be decorated), returns another function, the wrapper function
    def wrapper(*args): #function to be returned by decorator, it's where we will run our original function from
        print("Checking Somethings Before Function runs")
        print("Everything Okay, function can run")
        if (args[0] == 5):
            print('Function is right and can run')
            print(f'Function running {funcArg(*args)}')
        print("Function imekimbia mbio sana")
    return wrapper


@mydecorator
def add(x,y):
    return x+y

# add(10,6)


# A decorator: a function that takes another function as an argument and then, it adds some functionality to this new function

# mydecorator(add)

# @randomName the @ here means that randomName is a decorator function, it will randomFunc and add some functionality to it
# @randomName
# def randomfunc():
#     return 0

# @adminonly
# def accessrecords():
    # fuction to access sensitive records



def decoratorFunc(ourFunction): #this is the decorator func, it takes a function as an argument, and it returns a function
    # wrapper function to add functionality to the function we want to decorate
    def wrapper(*args,**kwargs):
        print("Function is starting to run now.....")
        # run the actual function
        ourFunction(*args, **kwargs)
        print("Function imekimbia ....., Good luck catching It!!!")
    return wrapper

@decoratorFunc
def say_hi(greeted_person):
    # ipdb.set_trace()
    print( f"I have been told to say Hi {greeted_person}!")

say_hi("Mercy")

@decoratorFunc
def add(x,y):
    return x+y

add(20,30)
    



