print("REPLIT LOGIN SYSTEM")

def login():
  while True:
    username = input("What is your username: ")
    password = input("What is your password: ")
    if username == "david" and password == "baldies4life":
      print("Welcome to REPLIT!")
      break
    else:
      print("Whoops! I don't recognise that username or password, try again")
      continue

login()