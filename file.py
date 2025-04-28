import os

def run_code(user_code):
    eval(user_code)  # Codacy will flag this as dangerous

user_input = input("Enter a filename: ")
os.system("cat " + user_input)

