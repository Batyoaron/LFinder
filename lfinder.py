import pyfiglet
import os
 

if os.path.isfile("laterdel.txt"):
    os.remove("laterdel.txt")
 
os.system('clear')
print("\033[1;32;40m \n")
ascii_banner = pyfiglet.figlet_format("LFinder")
print(ascii_banner)

print("\033[1;30;40m \n")
print('tip: paste the link into google, and it will tells you it is a virus or not')
print("\033[1;30;40m \n")
print('')


###data getharing

weba = input('This link contains "jd8wbd" similar words? y / n : ')

print('')

webb = input('the link has like this? [example.com-example-hello] y / n : ')

print("")

webc = input('you know the website that the link is contains? y / n : ')

print('')



##checking

if weba == "y":
    if webb == "n":
        if webc == "n":
            tts = input('you know the person how sent you the link? y / n : ')
            print('')
           
            if tts == "n":
                ttss = input('the link is contains long "HsukdJeo729jd=iwb82" characters like this? y / n : ')
                if ttss == "y":
                    print("\033[1;31;40m \n")
                    print('RISK: VERY HIGH')
                    print('Probably: you can get malware from that link / or like a ransomware')
                    exit()


if weba == "y":
    webaa =input('the link has LONG characters like this: [ow8heKe9Gk=kw92B]? y / n : ')
    print('')
    webab = input('you got the link from your enemy? or like from google, facebook? y / n :')
    
    if webaa == "y":
        if webaa == "y":
            print("\033[1;31;40m \n")
            print('RISK: HIGH')
            print('it can be anything in that link')
            exit()


if weba == "y":
    if webb == "y":
        if webc == "y":
            print("\033[1;34;40m \n")
            print('risk: medium')
            print('even your freinds can be dangerous')
            exit()

    
                       
if weba == "n":
    if webb == "y":
        if webc == "n":
            print("\033[1;33;40m \n")
            print('risk: low-medium')
            print('i dont know. paste it into google and it will tells you it is virus or not, but i dont think so it is harmful')
            exit()   
                      
                               
if weba == "y":
        if webc == "n":
            print("\033[1;33;40m \n")
            print('risk: medium')
            print('probably iplogger')
            
            exit()
            
            
if weba == "y":
        if webc == "n":
            print("\033[1;33;40m \n")
            print('risk: medium')
            print('probably iplogger')
            exit()
            
        
###link is good

if weba == "y":
    if webb == "n":
        if webc == "y":
            print("\033[1;32;40m \n")
            print('risk: low')
            print('hmm.... probably an invite?')
            exit()
            


if weba == "n":
            if webb == "n":
                if webc == "y":
                    if webb == "n":
                        
                        print("\033[1;32;40m \n")
                        print('no risk')
                        print('oppening: safe')
                        exit()
                        
                        
if weba == "n":
    print("\033[1;32;40m \n")
    print('no risk')
    print('oppening: safe')
    exit()      
    
      
if weba == "n":
    if webb == "y":
        if webc == "n":
            print("\033[1;32;40m \n")
            print('risk: low')
            print('if the link doesnt have [jeKei72h] characters like this, it means probably safe')
            
            exit()

            
                        
##error

print("\033[1;31;40m \n")
print('something went wrong ):') 
