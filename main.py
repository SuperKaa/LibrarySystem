import json
import time
from colorama import *
import os

init(autoreset = True)

def clear():
    os1 = os.name
    if os1 == "nt":
        os.system("cls")
    else:
        os.system("clear")

with open("data.json", "r") as file:
    data = json.load(file)

def findborrower(book):
    for student, info in data["students"].items():
        if info["borrowed"] == book:
            return student
    return Fore.RED + "-error not found-"

def borrowbook(student, book):
    global data

    student = student.lower()
    book = book.lower()

    if student in data["students"]:
        time.sleep(0.5)
        print(Fore.GREEN + f"student {student} found")
        studentfound = True
    elif student not in data["students"]:
        time.sleep(0.5)
        print(Fore.RED + f"student {student} not found!")
        studentfound = False

    if studentfound == True:
        if book in data["books"]:
            time.sleep(0.5)
            print(Fore.GREEN + f"book {book} found")
            if data["books"][book]["status"] == "available":
                time.sleep(0.5)
                print(Fore.GREEN + f"book {book} is available for borrowing")

                data["books"][book]["status"] = "borrowed"

                data["students"][student]["borrowed"] = book
 
                time.sleep(0.5)
                print(Fore.GREEN + f"{book} successfully taken by {student}")

            elif data["books"][book]["status"] == "borrowed":

                currentborrower = findborrower(book)

                time.sleep(0.5)

                print(Fore.RED + f"the book is currently take out by {currentborrower}")

        elif book not in data["books"]:
            time.sleep(0.5)
            print(Fore.RED + f"book {book} not found")

def returnbook(student, book):
    global data

    student = student.lower()
    book = book.lower()

    if student in data["students"]:
        time.sleep(0.5)
        print(Fore.GREEN + f"student {student} found")
        studentfound = True
    elif student not in data["students"]:
        time.sleep(0.5)
        print(Fore.RED + f"student {student} not found!")
        studentfound = False

    if studentfound == True:
        if book in data["books"]:
            time.sleep(0.5)
            print(Fore.GREEN + f"book {book} found")
            if data["books"][book]["status"] == "borrowed":

                data["books"][book]["status"] = "available"

                data["students"][student]["borrowed"] = ""

                time.sleep(0.5)

                print(Fore.GREEN + f"{book} successfully returned by {student}")

            elif data["books"][book]["status"] == "available":

                time.sleep(0.5)

                print(Fore.YELLOW + "the book is already with the library")

        elif book not in data["books"]:
            time.sleep(0.5)
            print(Fore.RED + f"book {book} not found")

def addstudent(student):
    global data

    if student in data["students"]:
        print(Fore.RED + f"{student} already exists")

    elif student not in data["students"]:
        data["students"][student] = {"borrowed": ""}
        print(Fore.GREEN + f"{student} added into database")

def removestudent(student):
    global data

    if student in data["students"]:
        print(Fore.GREEN + f"{student} found")

        del data["students"][student]

        print(Fore.GREEN + f"{student} removed")

    elif student not in data["students"]:

        print(Fore.RED + f"{student} not found")

def addbook(book):
    global data

    if book in data["books"]:
        print(Fore.RED + "Book already exists")

    elif book not in data["books"]:
        data["books"][book] = {"status": "available"}
        print(Fore.GREEN + f"{book} has been added")
    
def removebook(book):
    if book in data["books"]:
        print(Fore.GREEN + "book found")
        del data["books"][book]
        print(f"{book} has been deleted")

    elif book not in data["books"]:
        print(Fore.RED + "{book} not found")

def main():
    while True:
        clear()
        try:
            print(Fore.YELLOW + "-------------------------------------")
            print(Fore.CYAN + """     
   __ _ _                          
  / /(_) |__  _ __ __ _ _ __ _   _ 
 / / | | '_ \| '__/ _` | '__| | | |
/ /__| | |_) | | | (_| | |  | |_| |
\____/_|_.__/|_|  \__,_|_|   \__, |
                             |___/ 
""")
            print(Fore.YELLOW + "-------------------------------------")
            action = int(input(Fore.MAGENTA + """
1) add/remove students
2) add/remove books
3) borrow/return book
==> """))
            print(" ")
        except ValueError:
            print(Fore.RED + "please enter a number only")

        if action in [1,2,3]:
            break
        else:
            print(Fore.RED + "please choose 1, 2, 3")
            time.sleep(0.8)
    
    if action == 1:
        while True:
            choice = input(Fore.MAGENTA + "add or remove? ").lower()

            if choice in ["add", "remove"]:
                break
            else:
                print(Fore.RED + "please choose add or remove")

        student = input(Fore.MAGENTA + "whats the students first name? ").lower()
        
        if choice == "add":
            addstudent(student)
        elif choice == "remove":
            removestudent(student)

    elif action == 2:
        while True:
            choice = input(Fore.MAGENTA + "add or remove? ").lower()

            if choice in ["add", "remove"]:
                break
            else:
                print(Fore.RED + "please choose add or remove")

        student = input(Fore.MAGENTA + "whats the books name? ").lower()
        
        if choice == "add":
            addbook(student)
        elif choice == "remove":
            removebook(student)

    elif action == 3:
        while True:
            choice = input("borrow or return? ").lower()

            if choice in ["borrow", "return"]:
                break
            else:
                print(Fore.RED + "please choose borrow or return")

        student = input(Fore.MAGENTA + "whats the students first name?").lower()
        book = input(Fore.MAGENTA + "whats the books name? ").lower()
        
        if choice == "borrow":
            borrowbook(student, book)
        elif choice == "return":
            returnbook(student, book)
        


    time.sleep(0.5)
    print(Fore.MAGENTA + "saving data please dont close!")

main()

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
time.sleep(0.5)
print(Fore.GREEN + "successfully saved data")
