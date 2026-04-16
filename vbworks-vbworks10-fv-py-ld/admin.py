import time as t
#this is a dependency . 
consoleVer = '1.2.1'
#Dependency 1
admin_id = 'SD7Jf0 + UF9r'
def adminGame(): 
    type_the_fll = 'OFDJ56'
    print("Hello Admin! Let's check if you're actually an admin!")
    admin_id_check = input("Enter your ADMIN ID: ")
    if admin_id_check == admin_id:
        print(' ')
        print('Ok looks like you need to verify if you are a robot!')
        type_the_following = input('Type the following : OFDJ56 ')
        if type_the_following == type_the_fll:
            print('You have succeed, redirecting to ADMIN CONSOLE')
            print(' ')
            print('CONSOLE')
            console = input('(Type /help to start console) > ')
            if console == '/help':
                print('List of commands')
                print('/data - Provides console info')
                print('/logout - Log out of the admin console easily')
                print('/minigames - Play some minigames (not added to vbworks yet.)')
                print('Starting console...')
                inpu1 = input('> ')
                if inpu1 == '/data':
                    print('CONSOLE Ver' + consoleVer)
                    updte1 = input('Found new update. Want to install it? (y / n) ')
                    if updte1 == 'n':
                        print('Ok.')
                    if updte1 == 'y':
                        print('Installing...')
                        t.sleep(5)
                        print('Restarting console...')
                        print('< --------- Loading ---------- >')
                        print('Welcome back!')
                if inpu1 == '/logout':
                    print('Logging out...')
                    t.sleep(5)
    else:
        print('Incorrect id. ERROR CODE : IW283')
        t.sleep(2)
        print('Logging you out for security reasons')
        print('Logging out')
        t.sleep(2)
        print('Logged out!')

#Dependency - for VBWorks
#(C) WEP Tech, commAn Tech

# adminpy dep 1 for vbworks aka rluski



