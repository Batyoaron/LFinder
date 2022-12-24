####by batyoaron ######
import random
import os
import string
import time
import sys


a = randomLetter = random.choice(string.ascii_letters)


print("\033[1;32;40m")



os.system('clear')
ascii = '''


██╗░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██║░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██║░░░░░█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██║░░░░░██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
███████╗██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
'''
print(ascii)


print("\033[1;31;40m")
print('                                       LFinder v2.2')
print('                                       by: BatyoAron') 
print('                                       rateing: 0.0')
print("\033[1;30;40m \n")



link = input('type your LINK here: ')



#########################
######  Checking  ###########
##########################



if "https://" in link:
    print('check test 1: good')
else:
    if "http://" in link:
        print('check test 2: is good')
    else:
        if "www." in link:
            print('check test 3: good')
        else:
            print("\033[1;31;40m \n")
            print('bad link')
            time.sleep(1)
            os.execl(sys.executable, sys.executable, *sys.argv)           
        

       
        
print("\033[1;32;40m \n")
hline = '''
________ Log _________________________
'''

print(hline)              

###data of the harmfull website      
      
if ".ngrok.io" in link:
            print("\033[1;31;40m")
            print('Risk: medium-High')
            print('')
            print('data: Ngrok links probably(80%) dangerous')
            exit()
            

if "http://" in link:
    
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: links that contain http instead of https it means that if hackers steal the website database, your password is getting leaked')
    print('')
    print('')
    print('data 2:')    
    print('')
    
if ".com-" in link:
    if "@is.gd/" in link:
        print("\033[1;31;40m")
        print('Risk: High')
        print('data: Phishing')    
        exit()
        
if "trycloudflare.com" in link:
    print("\033[1;31;40m")
    print('risk: high')
    print('Data: phishing')
    exit()

if "ihr.life" in link:
    print("\033[1;31;40m")
    print('risk: high')
    print('Data: phishing') 
    exit()
                                                                              
#ip logger
    
if "wg.gl" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()            

    
if "ed.tc" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()            

    
if "iplogger.org" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()    
    
    
if "iplogger.com" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()            
 
    
if "iplogger.ru" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()            
       
    
if "mapper.info" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()
    
    
if "iplogger.co" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger') 
    exit()           
            
    
if "2no.co" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')  
    exit()          
    
if "yip.su" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()
    
    
if "iplogger.info" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')   
    exit()         
            
    
if "ipgrabber.ru" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')       
    exit()     
    
if "ipgraber.ru" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')       
    exit()     
    
if "iplis.ru" in link:
    print("\033[1;33;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()
    
    
if "02ip.ru" in link:
    print("\033[1;32;40m")
    print('risk: medium')
    print('data: iplogger')      
    exit()      
            
    
if "ezstat.ru" in link:
    print("\033[1;32;40m")
    print('risk: medium')
    print('data: iplogger')
    exit()            



######## links that hard to solve




if "vm.tiktok.com/" in link:
    print("\033[1;32;40m")
    print('no risk')
    print('data: Someone sent you a video link')
    exit()
else:
    
    if "www.tiktok.com" in link:
            print("\033[1;32;40m")   
            print('no risk')
            print('data: popular social media application')
            exit()
    
    else:
        
        if "https://tiktok.com" in link:
            print("\033[1;32;40m")
            print('no risk')
            print('data: popular social media application')
            exit()
        else:
            if "tiktok" in link:
                print("\033[1;31;40m")
                print('risk: high')
                print('data: if you get this link on messenger: do not open that link, the person who sent you the link it means he is infected with a virus')
                exit()
    
            
    
    



############
###link is good #########
############



if link == "https://google.com":
    print("\033[1;32;40m")
    print('no risk')
    print('data: google is the most popular website / application in the world')
    exit()
    





if "https://www.facebook.com/profile.php?id=" in link:
    print("\033[1;32;40m")
    print('no risk')
    print('data: it is just a facebook profile')
    exit()

    
if "discord.gg/" in link:
    print("\033[1;32;40m")
    print('no risk')
    print('data: you got an invite to a server') 
    exit()   
#### not sure

if "www." in link:
    oneq = input('im not sure about it, it has custom name? y / n : ')
    
    if oneq == "y":
        print("\033[1;31;40m")
        print('risk: high?')
        print('data: dont open that link')
        exit()
    else:
        print("\033[1;32;40m")
        print('risk: low')
        print('data: paste it into google and it will tell you if it is dangerous or not')
        exit()
     
### no data
      
if "duckduckgo.com/" in link:
          print("\033[1;30;40m")
          print('private browser so it can be anything in that link, dont open it, come back in v4.0')
          print('data: dont open that link. tor browser has dark web so everything can be in that link')
          exit()
          
          
      
if ".onion" in link:
        print("\033[1;30;40m")
        print('tor browser dont supported, come back in v3.0')
        print('data: dont open that link. tor browser has dark web so everything can be in that link')
        exit()
        


    
print("\033[1;30;40m \n")
print('no data yet, come back in a later version (:')
print("")
input('enter to try again')
os.execl(sys.executable, sys.executable, *sys.argv)            

