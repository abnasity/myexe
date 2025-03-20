

# age = 25
# has_id = True

# if age >= 18 and has_id:
#     print("You can enter the club.")








calculation_to_units = 24
name_of_unit = "hours"
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
calculated_value = days_to_units(int(user_input))
print(calculated_value)


    # if num_of_days > 0:
    #     return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    # elif num_of_days == 0:
    #     return "you entered a 0, please enter a valid positive number"
    # else:
    #     return "you entered a negative number, no conversion for you!"