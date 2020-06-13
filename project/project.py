import requests
import json
import random
import os
import time
import sys
from termcolor import colored
from colorama import Fore
from colorama import Style


rap_singers =['joyner lucas', 'eminem','drake']
country_singers=['jhonny cash', 'george jones', 'john denver']
pop_singers = ['rihanna', 'miley cyrus', 'michael jackson','seleena gomez']
rock_singers = ['jet','soundgarden','dani california','The Killers']


score1 =0
class game():
    def __init__(self,score=0):
        self.score=score 
    def starting(self):
            
        while True:

            print()
            path = input('What genre do you like to guess from? Rap, Country, Pop or Rock  (q to quit) ')
            while path=="":
                path= input("Please enter a valid name ")
            print()
            if  path == "q" or path == "quit": 

                break                   


            files = os.listdir('songs/'+path)
            index = random.randrange(0, len(files))

            if path == "rap":
                with open('songs/rap/'+files[index] , 'r') as f:

                    x = f.read()
                    x=str(x)
                print(colored(x,'magenta' ))
   
                userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
  
                print("****" * 5)
                print("your answer is : " , userRes)
                artist=''
                rap_path='songs/rap/'+files[index]
                if rap_path=='songs/rap/whenimgone.txt':
                    
                    artist=rap_singers[1]
                if rap_path == 'songs/rap/ilove.txt':
                    
                    artist =rap_singers[0]
                if rap_path == "songs/rap/loseyourself.txt":
                
                    artist =rap_singers[1]
                if rap_path == "songs/rap/hotlinebling.txt":
                
                    artist =rap_singers[2]        
                if userRes == artist:
                    self.score +=100
                    print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')


                else:
                    if self.score != 0: 
                        self.score -=100
                    print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
                    print('')
                    print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}')
                
                            


            if path == "country":
                with open('songs/country/'+files[index] , 'r') as f:

                    x = f.read()  
                    x=str(x)
                print(colored(x,'magenta' ))
                userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
                print("****" * 5)
                print("your answer is : " , userRes)
                artist=''
                country_path='songs/country/'+files[index]
                if country_path=='songs/country/backhome.txt':
                    artist=country_singers[2]
                if country_path == 'songs/country/hurt.txt':
                    artist =country_singers[0]
                if country_path == "songs/country/raceison.txt":
                    artist =country_singers[1]  
                if userRes == artist:
                    self.score +=100
                    print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')
                else:
                    if self.score != 0: 
                        self.score -=100               
                    print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
                    print('')
                    print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}')

            if path == "pop":
                with open('songs/pop/'+files[index] , 'r') as f:

                    x = f.read()
                    x=str(x)
                    
                
                print(colored(x,'magenta' ))
                userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
                print("****" * 5)
                print("your answer is : " , userRes)
                artist=''
                pop_path='songs/pop/'+files[index]
                if pop_path=='songs/pop/thriling.txt':
                
                    artist=pop_singers[2]
                if pop_path == 'songs/pop/unfaithful.txt':
                    
                    artist =pop_singers[0]
                if pop_path == "songs/pop/wreckingball.txt":
                    
                    artist = pop_singers[1] 
                if pop_path == "songs/pop/boyfriend.txt":
                    
                    artist = pop_singers[3]                  
                if userRes == artist:
                    self.score +=100
                    print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')
                else:
                    if self.score != 0: 
                        self.score -=100
                    print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
                    print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}')      


            if path == "rock":
                with open('songs/rock/'+files[index] , 'r') as f:

                    x = f.read() 
                    x=str(x) 
                print(colored(x,'magenta' ))
                userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
                print("****" * 5)
                print("Your answer is : " , userRes)
                artist=''
                rock_path ='songs/rock/'+files[index]
                if rock_path=='songs/rock/are_u_gna_be_my_girl.txt':
                    artist= rock_singers[0]
                if rock_path == 'songs/rock/soundgarden.txt':
                    artist =rock_singers[1]
                if rock_path == "songs/rock/redhot.txt":
                    artist = rock_singers[2] 
                if rock_path == "songs/rock/foolagain.txt":
                    artist = rock_singers[3]                  
                if userRes == artist:
                    self.score +=100
                    print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')
                else:
                    if self.score != 0: 
                        self.score -=100
                    print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
                    print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}') 
            


            print('\nAgain? (y/n)')
            again = input(">")

            if again.lower() =="n"or again.lower()=='no':
                break





if __name__ == "__main__":
    new=game()
    new.starting()
  


 

