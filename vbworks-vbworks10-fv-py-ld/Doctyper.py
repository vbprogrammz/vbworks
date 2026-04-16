# Copyright (C) WEP Tech, commAn Tech
#Dependency 2
import time as t
def docTyper():
    def storeSomethingValue():
        print("Create a value to be stored in the computer")
        val1 = input("1. ")
        val2 = input("2. ")
        val3 = input("3. ")
    
        input("Hit enter when information is needed: ")
        print(val1)
        print(val2)
        print(val3)
    
    print("Connecting to DOCTYPER SYSTEM...")
    t.sleep(3)
    print("Libraries...")
    t.sleep(4)
    print("Type a document: ")
    title = input("Title of document: ")
    doctyped = input("Type your document here: ")
    saveorno = input("Do you want to save your document? ")
    no = "no"
    NO = "NO"
    yes = "yes"
    YES = "YES"
    if saveorno == no:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == NO:
        aresure = input("Ok. Are you sure?: ")
    if saveorno == YES:
        print("Ok.")
    if saveorno == yes:
        print("Ok.")

    storeSomething = input('Do you want to save something in the computer (Deletes after 1 min)')

    if storeSomething == 'yes':
        storeSomethingValue()
    if storeSomething == 'Yes':
        storeSomethingValue()
    if storeSomething == 'No':
        print('Ok.')
    if storeSomething == 'no':
        print('Ok.')
    
    print("Thank you for chosing Document Typer")


docTyper()
