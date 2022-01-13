# Functions in Python

# function declaration
def print_name(_name): # parametric function
    print("Hi!",_name + '.')

def add(num1 ,num2):
    answers = num1 + num2
    return answers 

def greet():
    print("Hi! Python.")

# function definition
greet()
print_name('Waleed')
print(add(12,2))

# school calculator program
# function

def school_age_calaulate(_userAge):
    if _userAge == 5:
        print("You can join the school")
    elif _userAge <= 12:
        print("Of'Course you can join the school")
    elif _userAge < 18:
        print("You can join the college | Higher Education")
    else:
        print("Sorry! you are still baby")

# function call
school_age_calaulate(12)

# future age function
def future_Age (_UserAge):
    _UserAge = _UserAge + 20
    return _UserAge

print("You future age is", future_Age(12))