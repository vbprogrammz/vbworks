# VB WORKS Dev mode - not for public
#Unless you are a programmer, please don't look at the code. It ruins some minigames...
#This is available on KhanAcademy.org  & Github too! (I would like it if somebody remixed and made this into a better project)
#Problem: Does not save password and username after creation
#Code: Copyright, (C) 2025 WEP Tech, commAn Tech
#Domain name example.com is not mine.
# I don't know why but I put variables for Sng and Lg
#I DONT HAVE ANY GOOD IDEAS AHHHHHHHH
#Removed error of retry of main loop (delayed so far)

admin_id = 'SD7Jf0 + UF9r'
import time
import random
from time import sleep
from admin import adminGame
import main2 

sng = "sng"
lg = "lg"
version = "v6" + ' Full Version - DEVLOPER MODE'

# main def for game (random game)

print("Welcome to VBWORKS " + version + " (v10 Full Licensed)")
#print(' Note: Leak of betas and unrealesed software can lead to termination of job. Please handle with care.')
print("Copyright, (C) 2025 WEP Technoligies, commAn Tech (REGD: SD7Jf0 + UF9r)")
print("")
print("Connecting to system...")
time.sleep(5)
print("Loading libraries...")
time.sleep(5)
print(" ")
print("Registration Process...")
time.sleep(2)
Registration = input("Login (If sign up type sng and hit enter if not "+
                         "type lg and hit enter Guest is g) ")
#sng reged
if Registration == sng:
    print("Sign up process...")
    time.sleep(2)
    nme_usrsmg = input("Name:")
    age_usrsmg = input("Age:")
    dmy_usrsmg = input("Date of Birth (D/M/Y): ")
    print("")
    print("Account Creation")
    usr_namesmg = input("Username: ")
    email_global = print("Your account is " + usr_namesmg + "/vbworks")
    password_acc = input("Choose a password: ")
    print("Account created! ")
    print("Welcome " + nme_usrsmg)

#LG REgistration
if Registration == lg:
    print("Log in")
    email_lg = input("Email: ")
    password_lg = input("Password: ")
    name_lg = input("Name: ")
    print("Loading...")
    time.sleep(5)
    print("Welcome back " + name_lg)

if Registration == 'g':
    print('Hello guest.')
    input('Username (Not your real name) : ')

print("")
ask_user_what = input("What do you want to do? "
+ "DocTyper, New Post, Game, Practice Sentences, The Database (Game 2) ")

def docTyper():
    print("Connecting to DOCTYPER SYSTEM...")
    time.sleep(5)
    print("Libraries...")
    time.sleep
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
    print("Create a value to be stored in the computer")
    val1 = input("1. ")
    val2 = input("2. ")
    val3 = input("3. ")
    
    input("Hit enter when information is needed: ")
    print(val1)
    print(val2)
    print(val3)
    
    print("Thank you for chosing Document Typer" + " " + version)


if ask_user_what == "DocTyper":
    docTyper()

if ask_user_what == "doc typer":
    docTyper()

if ask_user_what == "doctyper":
    docTyper()

if ask_user_what == "New Post":
    input("Name of post:")
    input("Type here:")
    print("")
    print("PUBLISHING")
    private_public = input("Private or Public? (pr for private " 
                           + "and pb for public)")
    if private_public == "pb":
        print("Post is public")
    
    if private_public == "pr":
        print("Post is private")

    print("")

if ask_user_what == "new post":
    input("Name of post:")
    input("Type here:")
    print("")
    print("PUBLISHING")
    private_public = input("Private or Public? (pr for private " 
                           + "and pb for public)")
    if private_public == "pb":
        print("Post is public")
    
    if private_public == "pr":
        print("Post is private")

    print("")

if ask_user_what == "game":
    numberSecret = random.randint(0, 10)
    guessGameAsk1 = input('Guess a number from 0 to 10 ') 
    if guessGameAsk1 == numberSecret:
        print('Congrats you won!')
    else:
        print('Sorry you lost! Better luck next time...')
        print('The number was: ' + str(numberSecret))
        sleep(4)

if ask_user_what == 'admin': 
    #this is a dependency . 
    consoleVer = '1.2.1'
    #Dependency 1
    admin_id = 'SD7Jf0 + UF9r'
    adminGame()

if ask_user_what == 'practice sentences':
    print("PRACTICE SENTENCES (Hit enter to skip)")
    print("New added everyday!")
    sent1 = print("The sun was bright, filled with the orange color. " + 
          "Samuel was astonished and loved the orange color")
    input("A. ")
    print("I love butter. Butter is good on bread, it is creamy and juicy. ")
    input("A. ")
    print(" ")
    print('Thanks for using PRTYPER')

if ask_user_what == 'the database' and 'the database game' and 'thedatabase':
    print('WAR is going on between your country and another country. Your job is to hack into their system and defuse their misiles. You can sabotage your country later on! Make use of all the features given to you in the console - Seagent 101')
    sleep(4)
    def helpg():
        print("LIST OF FUNCTIONS:")
        print("/chtgrp | See Chat Group.")
        print("/str | Store a value")
        print("/hack.admin | Hacks a random person")
        print("/help | For list of functions")

    def hack():
        print("Hacking....")
        sleep(7)
        print("Hacked.")

    def chat():
        print("@them2749: Hey let's hack @cakelover45")
        sleep(3)
        print("@thehacker: OKK")
        sleep(2)
        print("@cakelover45: What are u guys doin")
        sleep(3)
        print("@thehacker: nothin")

    def sstr():
        print("What value is to be stored:")
        str1 = input("1... ")
        str2 = input("2... ")
        str3 = input("3... ")
        input("Click enter when needed: ")
        print(str1)
        print(str2)
        print(str3)

    def attacked():
        print("1. Launch a nuke")
        print("2. Sabotage your team and help the others")
        #cntinue later

    # Actual code :) 

    first = input("> (Type /help for help) ")
        
    if first == "/help":
        helpg()
        
    if first == "/hack.admin":
        hack()
        
    if first == "/str":
        sstr()
        
    if first == "/chtgrp":
        chat()
    
    second = input("> (Type /help for help) ")
        
    if second == "/help":
        helpg()
        
    if second == "/hack.admin":
        hack()
        
    if second == "/str":
        sstr()
        
    if second == "/chtgrp":
        chat()
    
    three = input("> (Type /help for help) ")
        
    if three == "/help":
        helpg()
        
    if three == "/hack.admin":
        hack()
        
    if three == "/str":
        sstr()
        
    if three == "/chtgrp":
        chat()

    print("Oh NO a country is atacking your teritory look at the following" 
      + " options")
    attacked()
    ans = input("(1/2)")
    if ans == "1":
        print("You became loyal to your teritory GAME ENDING : LOYAL ENDING")
    if ans == "2":
        print('You have a few options!')
        print(' 1 - Help the country with your country\'s missiles and ammunition')
        print(' OR ')
        print(' 2 - Sabotoge the country and become a spy from your country!')
        askForOptionSabotage = input('1 / 2 ')
        if askForOptionSabotage == "2":
                print("You have become a spy for the other country. You are now a winner to your country. GAME ENDING : Happy ending!")
        if askForOptionSabotage == "1":
            print('You are now a rival to your own country. GAME ENDING: Hatred ending')

def copyrightNotice(year, company):
    print("(C) " + str(year) + " " + str(company) + "All rights reserved") 

copyrightNotice(2026, "WEP Technologies")
#(C) 2026 WEP Technologies 
# removed most bugs 
# admin py importing?
