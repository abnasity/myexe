
# guess = 9
# guess_count = 0
# guess_limit = 3
# while guess :
#     if  guess_count < guess_limit: 
#      print("you won!")
#     guess_count += 1
# else:
#     print("you failed!")
    
    
    
    
    
    
    
    
    
    
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#        print("you won!")
#        break
# else:
#     print("you failed!")


    
# command = ""
# while True:
#     command = input("> ")
#     if command == "start":
#       print("start the car....")
#     elif command == "stop":
#       print("car stopped ...")
#     elif command == "quit":
#       print("quit")
#     elif command == "help":
#         print("""
#  start - start the car
#  stop - stop the car
#  quit - quit             
#               """)
#     elif command == "quit":
#         break
#     else:
#         print("i dont understand that")
    
    
    
# command = ""

# while True:
#     command = input("> ").lower
    
#     if command == "start":
#         print("start the car")
#     elif command == "stop":
#         print("stop the car")
#     elif command == "quit":
#         print("quit")
#     elif command == "help":
#         print("""
# start - start the car
# stop - stop the car
# quit - quit
#               """)
        
#     elif command == "quit":
#         break
#     else:
#       print("game ended")
    
    
    
    
    
    
command = ""
while command != "quit":
    command = input("> ")
    if command == "start":
        print("start the car.....")
    elif command == "stop":
        print("stop the car....")
    elif command == "help":
        print(""""
"start - start the car "           
"stop - stop the car "          
"quit - quit"         
       """ )
    elif command == "quit":
        print("quit")