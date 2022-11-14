import pyfiglet
import os
 

if os.path.isfile("laterdel.txt"):
    os.remove("laterdel.txt")
 
os.system('clear')
print("\033[1;32;40m \n")
ascii_banner = pyfiglet.figlet_format("LFinder")
print(ascii_banner)

print("\033[1;30;40m \n")
print('tip: illeszd be googleba és megfogja mondani hogy vírus vagy nem')
print("\033[1;30;40m \n")
print('')


###data getharing

weba = input('a link tartalmaz "jd8wbd" ilyesmi karaktereket? y / n : ')

print('')

webb = input('tartalmaz ilyet a link? [példa.com-example-hello] y / n : ')

print("")

webc = input('ismered azt a weboldalt amit a link tartalmaz? y / n : ')

print('')



##checking

if weba == "y":
    if webb == "n":
        if webc == "n":
            tts = input('ismered az embert aki küldte neked? y / n : ')
            print('')
           
            if tts == "n":
                ttss = input('a link tartalmaz HOSSZÚ  "HsukdJeo729jd=iwb82" ilyen karaktereket? y / n : ')
                if ttss == "y":
                    print("\033[1;31;40m \n")
                    print('Kockázat: NAGYON MAGAS')
                    print('valószínüleg: kaphatsz malwaret abbol a linkből, vagy akár zsarolóvírust')
                    exit()


if weba == "y":
    webaa =input('a link tartalmaz ilyen HOSSZÚ össze visszaságot: [ow8heKe9Gk=kw92B]? y / n : ')
    print('')
    webab = input('a linket az ellenségedtől kaptad, vagy akár a googletól, a facebooktól? y / n :')
    
    if webaa == "y":
        if webaa == "y":
            print("\033[1;31;40m \n")
            print('KOCKÁZAT: MAGAS')
            print('bármi lehet abban a linkben')
            exit()


if weba == "y":
    if webb == "y":
        if webc == "y":
            print("\033[1;34;40m \n")
            print('kockázat: közepes')
            print('a barátaid is lehetnek veszélyesek')

    
                       
if weba == "n":
    if webb == "y":
        if webc == "n":
            print("\033[1;33;40m \n")
            print('kockázat: alacsony-közepes')
            print('nem tudom. illeszd be googleba és megfogja mondani hogy vírus-e vagy nem')
            exit()   
                      
                               
if weba == "y":
        if webc == "n":
            print("\033[1;33;40m \n")
            print('kockázat: közepes')
            print('valószínüleg iplogger')
            
            exit()
            
            
if weba == "y":
        if webc == "n":
            print("\033[1;33;40m \n")
            print('kockázat: közepes')
            print('valószínüleg iplogger')
            exit()
            
        
###link is good

if weba == "y":
    if webb == "n":
        if webc == "y":
            print("\033[1;32;40m \n")
            print('kockázat: alacsony')
            print('hmm.... valószínüleg egy meghívó?')
            exit()
            


if weba == "n":
            if webb == "n":
                if webc == "y":
                    if webb == "n":
                        
                        print("\033[1;32;40m \n")
                        print('nincs kockázat')
                        print('megnyitás: biztonságos')
                        exit()
                        
                        
if weba == "n":
    print("\033[1;32;40m \n")
    print('nincs kockázat')
    print('megnyitás: biztonságos')
    exit()      
    
      
if weba == "n":
    if webb == "y":
        if webc == "n":
            print("\033[1;32;40m \n")
            print('kockázat: alacsony')
            print('általába ha a linkeknek nincsenek [jeKei72h] ilyen karaktereik akkor biztonságosak(kivéve: meghívók)')
            
            exit()

            
                        
##error

print("\033[1;31;40m \n")
print('valami probléma történt ):') 
