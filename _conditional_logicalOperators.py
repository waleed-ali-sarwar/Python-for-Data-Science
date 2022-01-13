# Conditional in Python

# Eqaul to                        ==
# Greater than                    >
# Less than                       <
# Less than and equal to         <=
# Greater than and equal to      >=
# Not Equal to                   !=

# Exapmle

print(4 == 4) # Equal to
print(5 < 4) # less than
print(5 > 4) # Greater than
print(5 != 4) # Not Equal to
print(5 >= 4) # Greater than Equal to
print(5 <= 4) # Less than Equal to

# Applications of Logical operators

_age_At_School = 5
_user_Age = 4
print("Response:",_age_At_School == _user_Age)
print("Type of datatype is : ",type(_user_Age))
print("Type of datatype is : ",type(_age_At_School))

# input function and logical operator

_eligible_Age = 10
_inputUser_Age = input("HOw old are you ? ")
print("_InputUser_Age Type of datatype is : ",type(_inputUser_Age))
print(_inputUser_Age == _eligible_Age)

_inputUser_Age = input("Again How old are you ? ")
_inputUser_Age = int(_inputUser_Age)
print("_InputUser_Age Type of datatype is : ",type(_inputUser_Age))
print(_inputUser_Age == _eligible_Age)







