#BMI CALCULATOR
def bmi_func():
    user_height = float(input("Enter the Height: "))
    user_weight = float(input("Enter the Weight: "))
    print(bmi_calci(user_height,user_weight))


def bmi_calci(user_height, user_weight):
    return (user_weight/(user_weight*user_height))



# For BMI Calculator Enter 0
func_exercise = int(input("Enter the funcation number you wanted to execute: "))

match func_exercise:
    case 0:
        bmi_func()

