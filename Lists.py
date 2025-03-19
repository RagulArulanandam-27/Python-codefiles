import passport
import datetime 

# guido = passport.Passport("Guido", "van Rossum", "1956-01-31", "The Netherlands", "1999-03-20")
# print("Name:", 'Guido' in vars(guido).values())
# print("Surname:", 'van Rossum' in vars(guido).values())
# print("Dob:", datetime.date(1956, 1, 31) in vars(guido).values())
# print("Country:", 'The Netherlands' in vars(guido).values())
# print("Exp. date:", datetime.date(1999, 3, 20) in vars(guido).values())

# print(datetime.date(1999, 3, 20))
# print(vars(guido).values())

# codegrade = passport.Passport("Code", "Grade", "2017-07-21", "The Netherlands", "2999-12-31")
# countries = list(codegrade.countries_visited())
# print(countries)
# codegrade.stamp("The Netherlands")
# countries = list(codegrade.countries_visited())
# print(countries)
# codegrade.stamp("France")
# countries = list(codegrade.countries_visited())
# print(countries)
# codegrade.stamp("France")
# countries = list(codegrade.countries_visited())
# print(countries)
# codegrade.stamp("Germany")
# print("Germany" in list(codegrade.countries_visited()))
# print("France" in list(codegrade.countries_visited()))
# print("The Netherlands" in list(codegrade.countries_visited()))
# codegrade.stamp("Germany")
# print(len(list(codegrade.countries_visited())))
# codegrade.stamp("France")
# codegrade.stamp("Poland")
# print(len(list(codegrade.countries_visited())))
# []
# []
# ['France']
# ['France']
# True
# True
# False
# 2
# 3

# codegrade = passport.Passport("Code", "Grade", "2017-07-21", "The Netherlands", "2999-12-31")
# print(codegrade.passport_number())
# codegrade2 = passport.Passport("Code", "Grade2", "2017-07-21", "The Netherlands", "2999-12-31")
# print(codegrade2.passport_number())
# print(codegrade.passport_number())
# codegrade3 = passport.Passport("Code", "Grade3", "2017-07-21", "The Netherlands", "2999-12-31")
# codegrade4 = passport.Passport("Code", "Grade4", "2017-07-21", "The Netherlands", "2999-12-31")
# codegrade5 = passport.Passport("Code", "Grade5", "2017-07-21", "The Netherlands", "2999-12-31")
# codegrade6 = passport.Passport("Code", "Grade6", "2017-07-21", "The Netherlands", "2999-12-31")
# print(codegrade6.passport_number())
# print(codegrade.passport_number())

codegrade = passport.Passport("Code", "Grade", "2017-07-21", "The Netherlands", "2999-12-31")
codegrade.stamp("France")
print(codegrade.sum_square_visits())
codegrade.stamp("France")
print(codegrade.sum_square_visits())
codegrade.stamp("France")
print(codegrade.sum_square_visits())
codegrade.stamp("Germany")
codegrade.stamp("Germany")
print(codegrade.sum_square_visits())
codegrade.stamp("Poland")
print(codegrade.sum_square_visits())
codegrade.stamp("Poland")
print(codegrade.sum_square_visits())