"""
Design a program that sums all of the numbers entered by the user while ignoring any input that is not a valid number. Your program should display the current sum after each number is entered. It should display an appropriate message containing the word 'invalid' after each non-numeric input, and then continue to sum any additional numbers entered by the user. Exit the program when the user enters a blank line. Your program should just work with integers, and it must use exception handling to obtain its functionality.

Your program should stop only when 0 is entered.
"""


# total = 0

# while True:
#     user_input = input("Enter a number (or 0 to exit): ").strip()

#     # Exit the program when the user enters 0
#     if user_input == '0':
#         print("Total:", total)
#         break

#     try:
#         # Try converting input to an integer
#         number = int(user_input)
#         total += number
#         print(f"Current Total: {total}")
#     except ValueError:
#         # Handle invalid input by catching the exception
#         print("Invalid input. Please enter a valid number.")


# class NotABananaError(Exception):

#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# def am_I_a_banana(user_input: str):
#     if "banana" not in user_input:
#         raise NotABananaError(f"{user_input} is not a banana")
#     elif user_input == "banana":
#         return "Just banana"
#     else:
#         return "Not just banana"


# if __name__ == "__main__":
#     print(am_I_a_banana("banana"))

class InvalidGradeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def grade_points_to_letter(points):
    if points in range(0, 41):
        return "F"
    elif points in range(40, 51):
        return "D"
    elif points in range(50, 61):
        return "C"
    elif points in range(60, 71):
        return "B"
    elif points in range(70, 81):
        return "A"
    elif points in range(80, 100):
        return "A+"
    else:
        raise InvalidGradeError("Grade points out of valid range.")


def letter_to_grade_points(grade_point: str):
    grade = grade_point.strip().upper()

    match grade:
        case "F":
            return 0-40
        case "D":
            return 40-50
        case "C":
            return 50-60
        case "B":
            return 60-70
        case "A":
            return 70-80
        case "A+":
            return "80+"
        case _: raise InvalidGradeError("Invalid grade points")


while True:
    user_input = input()

    if user_input == "" or user_input.lower() == "end":
        break

    try:
        try:
            gp = int(user_input)
            letter_gp = grade_points_to_letter(gp)
            print(letter_gp)
        except ValueError:
            try:
                letter_gp = user_input.strip()
                print(letter_to_grade_points(letter_gp))
            except InvalidGradeError as ex:
                raise ex
    except Exception as ex:
        raise ex
