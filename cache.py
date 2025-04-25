# def get_input():
#     #Checking Q value is used to terminate the operation
#     input_value = input()
#     if (input_value.upper() == "Q"):
#         return 0
#     #converting input_value as integer to check the conditions.
#     input_page = int(input_value)
#     if input_page < 0:
#         print("Enter a positive value")
#         return 0
#     else:
#         return input_page




# def cache_program():
#     while True:
#         input_page = get_input() 
#         if(input_page == 0):
#             break
#         request_list=[]

#         while input_page != 0:
#             request_list.append(input_page)
            
#             input_page = get_input()
#             if(input_page == 0):
#                 break
        
#         cache_list = []
#         cache_len = 8

#         for input_page in request_list:
#             if input_page in cache_list:
#                 print("hit")
#             else:
#                 print("miss")
#                 if len(cache_list) >= cache_len:
#                     cache_list.pop(0)
#                 cache_list.append(input_page)
        
#         print(cache_list)


d = {
            1: ['A', 'C', 'B', 'D'],
            2: ['A', 'B', 'D', 'C'],
            3: ['C', 'B', 'A', 'D'],
            4: ['B', 'A', 'D', 'C']
        }
unique_list = set()
for pref in d.values():
    for canditate in pref:
        unique_list.add(canditate)


print(list(unique_list))
