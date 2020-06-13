# from random import randint
# from asciimatics.screen import Screen
import requests
import json
import random
import os
# from faker import Faker
# from assest import *
import time
import sys
from termcolor import colored
from colorama import Fore
from colorama import Style

# def demo(screen):
#     while True:
#         screen.print_at('Hello world!',
#                         randint(0, screen.width), randint(0, screen.height),
#                         colour=randint(0, screen.colours - 1),
#                         bg=randint(0, screen.colours - 1))
#         ev = screen.get_key()
#         if ev in (ord('Q'), ord('q')):
#             return
#         screen.refresh()

# Screen.wrapper(demo)

# from asciimatics.effects import Cycle, Stars
# from asciimatics.renderers import FigletText
# from asciimatics.scene import Scene
# from asciimatics.screen import Screen

# def demo(screen):
#     effects = [
#         Cycle(
#             screen,
#             FigletText("ASCIIMATICS", font='big'),
#             int(screen.height / 2 - 8)),
#         Cycle(
#             screen,
#             FigletText("ROCKS!", font='big'),
#             int(screen.height / 2 + 3)),
#         Stars(screen, 200)
#     ]
#     screen.play([Scene(effects, 500)])
#     ev = screen.get_key()

#     if ev in (ord('Q'), ord('q')):
#          return
#     screen.refresh()

# Screen.wrapper(demo)
# from gtts import gTTS 
# import os
# import winsound

# from playsound import playsound
# import os
# os.system("start C:\Users\s.allaham\codefellows\401\project")
# playsound('voice.mp3')

# file = open("lyrics/all_i_wanted.txt", "r").read().replace("\n", " ")
# language = "en"

# speech = gTTS(text = str(file), lang = language, slow = False)

# speech.save("voice.mp3")
# os.system("start voice.mp3")

# s = Sound() 
# s.read('voice.mp3') 
# s.play()

# import pyglet

# music = pyglet.resource.media('voice.mp3')
# music.play()

# pyglet.app.run()
# from asciimatics.effects import Print
# from asciimatics.renderers import BarChart, FigletText
# from asciimatics.scene import Scene
# from asciimatics.screen import Screen
# from asciimatics.exceptions import ResizeScreenError
# import sys
# import math
# import time
# from random import randint


# def fn():
#     return randint(0, 40)


# def wv(x):
#     return lambda: 1 + math.sin(math.pi * (2*time.time()+x) / 5)


# def demo(screen):
#     scenes = []
#     if screen.width != 132 or screen.height != 24:
#         effects = [
#             Print(screen, FigletText("Resize to 132x24"),
#                   y=screen.height//2-3),
#         ]
#     else:
#         effects = [
#             Print(screen,
#                   BarChart(10, 40, [fn, fn],
#                            char="=",
#                            gradient=[(20, Screen.COLOUR_GREEN),
#                                      (30, Screen.COLOUR_YELLOW),
#                                      (40, Screen.COLOUR_RED)]),
#                   x=13, y=1, transparent=False, speed=2),
#             Print(screen,
#                   BarChart(
#                       13, 60,
#                       [wv(1), wv(2), wv(3), wv(4), wv(5), wv(7), wv(8), wv(9)],
#                       colour=Screen.COLOUR_GREEN,
#                       axes=BarChart.BOTH,
#                       scale=2.0),
#                   x=68, y=1, transparent=False, speed=2),
#             Print(screen,
#                   BarChart(
#                       7, 60, [lambda: time.time() * 10 % 101],
#                       gradient=[
#                           (33, Screen.COLOUR_RED, Screen.COLOUR_RED),
#                           (66, Screen.COLOUR_YELLOW, Screen.COLOUR_YELLOW),
#                           (100, Screen.COLOUR_WHITE, Screen.COLOUR_WHITE),
#                       ] if screen.colours < 256 else [
#                           (10, 234, 234), (20, 236, 236), (30, 238, 238),
#                           (40, 240, 240), (50, 242, 242), (60, 244, 244),
#                           (70, 246, 246), (80, 248, 248), (90, 250, 250),
#                           (100, 252, 252)
#                       ],
#                       char=">",
#                       scale=100.0,
#                       labels=True,
#                       axes=BarChart.X_AXIS),
#                   x=68, y=16, transparent=False, speed=2),
#             Print(screen,
#                   BarChart(
#                       10, 60,
#                       [wv(1), wv(2), wv(3), wv(4), wv(5), wv(7), wv(8), wv(9)],
#                       colour=[c for c in range(1, 8)],
#                       bg=[c for c in range(1, 8)],
#                       scale=2.0,
#                       axes=BarChart.X_AXIS,
#                       intervals=0.5,
#                       labels=True,
#                       border=False),
#                   x=3, y=13, transparent=False, speed=2)
#         ]

#     scenes.append(Scene(effects, -1))
#     screen.play(scenes, stop_on_resize=True)


# while True:
#     try:
#         Screen.wrapper(demo)
#         sys.exit(0)
#     except ResizeScreenError:
#         pass

# x='hello'

# input(x)
# rap_singers =['joyner lucas', 'eminem','drake']
# country_singers=['jhonny cash', 'george jones', 'john denver']
# pop_singers = ['rihanna', 'miley cyrus', 'michael jackson','seleena gomez']
# rock_singers = ['jet','soundgarden','dani california','The Killers']


# class game():
#     def __init__(self,score=0):
#         self.score=score 
#     def starting(self):
            
#         while True:
#             # if user_sats =='y':
#             print()
#             path = input('What genre do you like to guess Rap, Country ,Pop or Rock or q to quit ')
#             while path=="":
#                 path= input("Please enter a valid name ")
#             print()
#             if  path == "q" or path == "quit": 
#                 # print('Thanks for playing! Bye')   
#                 break                   

#             # path ='rap'
#             files = os.listdir('songs/'+path)
#             index = random.randrange(0, len(files))

#             if path == "rap":
#                 with open('songs/rap/'+files[index] , 'r') as f:

#                     x = f.read()
#                     x=str(x)
#                 print(colored(x,'magenta' ))
                    
#                 # print(x)
#                 userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
#                 # colored('\nSearch for Artist/Band ','green',attrs=['reverse', 'blink'])
#                 print("****" * 5)
#                 print("your answer is : " , userRes)
#                 artist=''
#                 rap_path='songs/rap/'+files[index]
#                 if rap_path=='songs/rap/whenimgone.txt':
                    
#                     artist=rap_singers[1]
#                 if rap_path == 'songs/rap/ilove.txt':
                    
#                     artist =rap_singers[0]
#                 if rap_path == "songs/rap/loseyourself.txt":
                
#                     artist =rap_singers[1]
#                 if rap_path == "songs/rap/hotlinebling.txt":
                
#                     artist =rap_singers[2]        
#                 if userRes == artist:
#                     self.score +=100
#                     print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')
#                     # print(colored('green', 'Well Done'))

#                 else:
#                     if self.score != 0: 
#                         self.score -=100
#                     print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
#                     print('')
#                     print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}')
                
                            


#             if path == "country":
#                 with open('songs/country/'+files[index] , 'r') as f:

#                     x = f.read()  
#                     x=str(x)
#                 print(colored(x,'magenta' ))
#                 userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
#                 print("****" * 5)
#                 print("your answer is : " , userRes)
#                 artist=''
#                 country_path='songs/country/'+files[index]
#                 if country_path=='songs/country/backhome.txt':
#                     artist=country_singers[2]
#                 if country_path == 'songs/country/hurt.txt':
#                     artist =country_singers[0]
#                 if country_path == "songs/country/raceison.txt":
#                     artist =country_singers[1]  
#                 if userRes == artist:
#                     self.score +=100
#                     print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')
#                 else:
#                     if self.score != 0: 
#                         self.score -=100               
#                     print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
#                     print('')
#                     print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}')

#             if path == "pop":
#                 with open('songs/pop/'+files[index] , 'r') as f:

#                     x = f.read()
#                     x=str(x)
                    
                
#                 print(colored(x,'magenta' ))
#                 userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
#                 print("****" * 5)
#                 print("your answer is : " , userRes)
#                 artist=''
#                 pop_path='songs/pop/'+files[index]
#                 if pop_path=='songs/pop/thriling.txt':
                
#                     artist=pop_singers[2]
#                 if pop_path == 'songs/pop/unfaithful.txt':
                    
#                     artist =pop_singers[0]
#                 if pop_path == "songs/pop/wreckingball.txt":
                    
#                     artist = pop_singers[1] 
#                 if pop_path == "songs/pop/boyfriend.txt":
                    
#                     artist = pop_singers[3]                  
#                 if userRes == artist:
#                     self.score +=100
#                     print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')
#                 else:
#                     if self.score != 0: 
#                         self.score -=100
#                     print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
#                     print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}')      


#             if path == "rock":
#                 with open('songs/rock/'+files[index] , 'r') as f:

#                     x = f.read() 
#                     x=str(x) 
#                 print(colored(x,'magenta' ))
#                 userRes = input(colored("Whos the singer?",'cyan',attrs=['reverse', 'blink']))
#                 print("****" * 5)
#                 print("Your answer is : " , userRes)
#                 artist=''
#                 rock_path ='songs/rock/'+files[index]
#                 if rock_path=='songs/rock/are_u_gna_be_my_girl.txt':
#                     artist= rock_singers[0]
#                 if rock_path == 'songs/rock/soundgarden.txt':
#                     artist =rock_singers[1]
#                 if rock_path == "songs/rock/redhot.txt":
#                     artist = rock_singers[2] 
#                 if rock_path == "songs/rock/foolagain.txt":
#                     artist = rock_singers[3]                  
#                 if userRes == artist:
#                     self.score +=100
#                     print(f'{Fore.GREEN}Great job! your score is : {self.score} {Style.RESET_ALL}')
#                 else:
#                     if self.score != 0: 
#                         self.score -=100
#                     print(f'{Fore.RED}Try again mate, your score is :{self.score}{Style.RESET_ALL}')
#                     print(f'The right answer is :{Fore.GREEN} {artist}{Style.RESET_ALL}') 
            
#             print()
#             print('scooooooooooore',self.score)
#             print('Again? (y/n)')
#             again = input(">")
#             if again =="n":
#                 break

# new=game()
# new.starting()
# print(new.score)
    # # print (a)

    # sep = '\n\n'
    # rest = data.split(sep, 1)[0]

    # # print('resssssssssssst',rest)

    


    # a=[]
    # a.append(rest.split(' '))
    # # old_val=a[0][8]
    # # print(a)
    # new_list=[]
    # new_list.extend([a[0][8],a[0][15]])
    # # t = list(map(lambda s: s.strip(), new_list))


    # a[0][8],a[0][15]='{ }','{ }'
    # print('olddddddddd',old_val)
    # /\r?\n|\r/


    # print(a[0][8])
    # # for char in a[0]:
    #     # print (char)
    # # print(new_list)
    # new_list = [item.replace("\n"," ") for item in new_list]
    # new_list = [item.replace(",","") for item in new_list]
    # new_list = [item.lower() for item in new_list]


    # separator = ' '
    # print('wooops',separator.join(a[0]))


    # for item  in new_list:

    #     question=input('whats the word? ')
    #     if question.lower() in new_list:
    #         print('well done')
    #     else:
    #         print('nope')
        
    # print('tttttttttttt',new_list)



# # strObj = "This is a sample string"
# newlyric=lyrics
# start = 150
# stop = 1000000
# # Remove charactes from index 5 to 10
# if len(newlyric) > stop :
#     newlyric = newlyric[0: start:] + newlyric[stop + 1::]

# print('newwwwwwwwwwww',newlyric)


# def game3():
#   while True:
#     print()
#     print("Welcome to the Musixmatch API explorer!")
#     print()
#     print("MENU OPTIONS")
#     print("1 - Search for the lyrics of a song")
#     print("0 - Exit")
#     print()
#     choice = input("> ")
#     print()

#     if choice == "0":
#         break

#     if choice == "1":
#         print("Whats's the name of the artist?")
#         artist_name = input("> ")
#         print("What's the name of the track?")
#         track_name = input("> ")
#         track_name= track_name.replace(" ", "_")
#         print()

#         path =f'jsonfiles/{track_name}.json'

#         if os.path.isfile(path):  
#             with open(path, 'r') as f:
#                dataa= f.read()
#             #    print('fffffffffffffffffffffff',dataa)
#                data = json.loads(dataa)
#                print(data['lyrics']['lyrics_body'])
#         else:  
#             api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
#             request = requests.get(api_call)
#             data = request.json()
#             data = data['message']['body']
#             data["artist_name"]=artist_name
#             data["song_name"] = track_name
#             # print(type(data))
#             print("API Call: " + api_call)
#             send_to_file = json.dumps(data)
#             i = input('would you like to store the data in json?')
#             if i == "yes":
#                 # json_list = []
#                 with open('jsonfiles/'+track_name+'.json', 'w') as f :
#                     f.write(send_to_file)  
#             print()
#             print(data['lyrics']['lyrics_body'])
          

#     print()
#     print("Again? (y/n) or guessing game")
#     again = input("> ")
#     if again == "n":    
#         break
#     if again =="guessing game":
#         game()


# def spinning_cursor():
#     while True:
#         for cursor in '|/-\\':
#             yield cursor

# spinner = spinning_cursor()
# for _ in range(20):
#     sys.stdout.write(next(spinner))
#     sys.stdout.flush()
#     time.sleep(0.1)
#     sys.stdout.write('\b')



# def who_to_call(user):
#     spinning_cursor()
#     # animation()
#     if user == "guessing game":
#         game()
#     elif user =="lyrics":
#         game3()     
#     else: 
#         print()
#         print('are you drunk?') 

# from itertools import groupby
# import random

# string='''samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham


# samer mohammed allaham
# samer mohammed allaham


# samer mohammed allaham
# samer mohammed allaham samer mohammed allaham samer mohammed allaham


# samer mohammed allaham
# samer mohammed allaham
# samer mohammed allaham
# '''
# li = string.splitlines() 

# # calculates the keys for each element present in iterable. It returns key and iterable of grouped items.
# res = [list(sub) for ele, sub in groupby(li, key = bool) if ele]

# random_lyric=random.choice(res)

# print('\nrandooooom lyric',random_lyric)

# separator = ', '

# full_text=separator.join(random_lyric)

# print('\nfulllll text',full_text)


# full_text_list=[]

# full_text_list.append(full_text.split())

# full_text_list = [item.replace(",","") for item in full_text_list[0]]

# print('\nfullltexxxt list',full_text_list)


# print('reeeeess',res)
 

# random_from_list=[]
# indexs=[]

# l = [len(element) for element in li] 

# # ask for defficulty based on input it changes the range of words 


# for item in range(4):

#     x=random.choice(full_text_list)

#     while x=='{ }' :
#         print('printing xxx111111',x)
#         x=random.choice(full_text_list)
#         if x!='{ }':
#             print('printing xxx2222222',x)
#             break
#         else:
#             continue

#     print('afterrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    

    
#     if x not in random_from_list:
#         try:
        
#             random_from_list.append(x)

#             print('insideee if checkng random',full_text_list.index(random_from_list[item]))
#             # change words to '{ }' based on index
#             print(random_from_list[item])
#             indexs.append(full_text_list.index(random_from_list[item]))
#             full_text_list[indexs[item]]='{ }'

#         except IndexError:
#             print('woops')

    
        

# full_text_list = [item.lower() for item in full_text_list]
# separator = ' '
# full_text_list=separator.join(full_text_list)



# answers=[]
# for item in random_from_list:
#     answers.append(item)


# for item  in range(4):
#     question=input('Guess the word: ')

#     question =question.replace(" ", "")
#     # out_of+=100

#     if question in  random_from_list:
#         # score+=100
#         print(colored(f'\nGood job,your score is\n','green'))


#         random_from_list.remove(question)
#     else:
#         print(colored(f'\nWrong answer, score is \n','red'))

# print(random_from_list)
# # full_text_list = full_text_list.replace('{ }', termcolor.colored('{ }', 'red'))