import os

"""
Function for running user code
"""
def run_code(user_code):
    eval(user_code)


user_input = input("Enter a filename: ")
os.system("cat " + user_input)

