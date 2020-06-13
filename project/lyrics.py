import lyricsgenius
from itertools import groupby
import random
import os
import termcolor
from termcolor import colored
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from gtts import gTTS 
import os
from project import *


score=0


def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("LYRICAL", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("GENIUSES!", font='big'),
            int(screen.height / 2 + 3)),
        Cycle(
            screen,
            FigletText("PRESS Q TO START", font='small'),
            int(screen.height / 2 + 12)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])

    ev = screen.get_key()
    
    if ev in (ord('Q'), ord('q')):
         return
    screen.refresh()

Screen.wrapper(demo)



lyrics=""
def get_data(singer_name='',song_name=''):
    
    genius = lyricsgenius.Genius("USho7r2sC5TnzfBariT40pSWNgzECt12OftUgwx0ncTO-U8DbG9YTpdKQkpVMKWW")

    genius.verbose = False

    genius.remove_section_headers = True

    singer_name=input(colored('\nSearch for Artist/Band ','green',attrs=['reverse', 'blink']))

    while singer_name=="" :
        singer_name=input('Please enter a name ')


    song_name=input(colored('\nSearch for Song ','green',attrs=['reverse', 'blink']))
    while song_name=="" :
        song_name=input('Please enter a name ')
        
    global lyrics

    song_name =song_name.replace(" ", "_")
    if os.path.isfile('lyrics/'+song_name+".txt"):

        lyrics = open('lyrics/'+song_name+".txt", "r")

        lyrics=str(lyrics.read())

    else:


        artist = genius.search_artist(singer_name, max_songs=1, sort="title")

        song = genius.search_song(song_name, artist.name)

        

        lyrics=song.lyrics
        song_name =song_name.replace(" ", "_")


        text_file = open('lyrics/'+song_name+".txt", "w")
        
        data=lyrics

        n = text_file.write(data)
        text_file.close()

    if play.lower()=='l' or play.lower()=='lyrics':

        return print(colored(lyrics,'magenta') )
    

out_of=0

def format_data(data =''):

    global lyrics

    data=lyrics


    def Cal_len(string): 
      
        # Using splitlines() divide into a list 
        li = string.splitlines() 

        #group by calculates the keys for each element present in iterable. It returns key and iterable of grouped items.
        # res makes a list of paragraphes
        res = [list(sub) for ele, sub in groupby(li, key = bool) if ele]

        # pick a random paragraph that is made as a list and divided as items
        random_lyric=random.choice(res)

        separator = ', '

        # join the paragraph to make it like a full text 
        full_text=separator.join(random_lyric)


        full_text_list=[]

        # seperate the paragraph to words
        full_text_list.append(full_text.split())

        full_text_list = [item.replace(",","") for item in full_text_list[0]]

        random_from_list=[]
        indexs=[]

        l = [len(element) for element in li] 

        # ask for defficulty based on input it changes the range of words 
        

        for item in range(4):

            x=random.choice(full_text_list)

            while x=='{ }' :
                x=random.choice(full_text_list)
                if x!='{ }':
                    break

            
            if x not in random_from_list:
                try:
                
                    random_from_list.append(x)
                    # change words to '{ }' based on index
                    indexs.append(full_text_list.index(random_from_list[item]))
                    full_text_list[indexs[item]]='{ }'
                except IndexError:
                    print('woops')
                

        full_text_list = [item.lower() for item in full_text_list]
        separator = ' '
        full_text_list=separator.join(full_text_list)

        full_text_list = full_text_list.replace('{ }', termcolor.colored('{ }', 'red'))



        print(f'\n{full_text_list}\n')
        random_from_list = [item.lower() for item in random_from_list]
        random_from_list = [item.replace(")","") for item in random_from_list]
        random_from_list = [item.replace("(","") for item in random_from_list]
        random_from_list = [item.replace("’","'") for item in random_from_list]
        random_from_list = [item.replace("?","") for item in random_from_list]
        random_from_list = [item.replace("!","") for item in random_from_list]
        random_from_list = [item.replace(".","") for item in random_from_list]

        answers=[]
        for item in random_from_list:
            answers.append(item)
        global score
        global out_of



        for item  in range(4):
            question=input('Guess the word: ')

            question =question.replace(" ", "")
            out_of+=100

            if question in  random_from_list:
                score+=100
                print(colored(f'\nGood job,your score is {score}\n','green'))


                random_from_list.remove(question)
            else:
                print(colored(f'\nWrong answer, score is {score}\n','red'))

        text = str(answers)

        text=colored(text,'cyan')

        score_text=str(score)

        score_text=colored(score_text,'green')

        out_of_text=str(out_of)

        out_of_text=colored(out_of_text,'green')

        print(f'\nThe answers are {text}, score is {score_text} / {out_of_text}\n')
        # Calculate length of each word 
        return l 
  
   
    Cal_len(data)




if __name__ == "__main__":

    print(colored('''\n                                                      Welcome to Lyrical Geniuses\n 
                   A fun game where you can either search for your favourite songs, play guess the Artist's name
                   or test your knowledge on how well you know your favourite songs with fill in the blanks.\n''','cyan'))
    
    while True:
        text='Type game1/g1 to play fill the words game, game2/g2 to play guess the artist game, l/lyrics to search for your favourtie songs and q/quit to quit '

        text = text.replace(' fill the words', termcolor.colored(' fill the words', 'magenta'))
        text = text.replace('game1/g1', termcolor.colored('game1/g1', 'magenta'))
        text = text.replace('guess the artist', termcolor.colored('guess the artist', 'yellow'))
        text = text.replace('game2/g2', termcolor.colored('game2/g2', 'yellow'))
        text = text.replace('search for your favourtie songs', termcolor.colored('search for your favourtie songs', 'blue'))
        text = text.replace('l/lyrics', termcolor.colored('l/lyrics', 'blue'))
        text = text.replace('q/quit to quit', termcolor.colored('q/quit to quit', 'red'))



        play=input(f'\n{text}\n')
        if play.lower()=='game1'  or play.lower()=='g1':
            get_data()
            format_data()
        elif play.lower()=='q' or play.lower()=='quit':
            try:
                score_from_project
            except NameError:
                score_from_project=0

            sum_=score+score_from_project
            text_sum=str(sum_)
            # text_sum=colored(text_sum,'green')
            
            def demo2(screen):
                global text_sum
                effects = [
                    Cycle(
                        screen,
                        FigletText("THANKS FOR PLAYING!", font='big'),
                        int(screen.height / 2 - 8)),
                    Cycle(
                        screen,
                        FigletText(f"YOUR FINAL SCORE IS {text_sum}", font='small'),
                        int(screen.height / 2 + 3)),
                    Cycle(
                        screen,
                        FigletText("PRESS Q TO EXIT", font='small'),
                        int(screen.height / 2 + 12)),
                    Stars(screen, 200)
                ]
                screen.play([Scene(effects, 500)])

                ev = screen.get_key()
                
                if ev in (ord('Q'), ord('q')):
                    return
                screen.refresh()

            Screen.wrapper(demo2)

    
            # print(f'\nThanks for playing! your total score in both games is {text_sum} \n')

            break
        elif play.lower()=='l' or play.lower()=='lyrics':
            get_data()
        elif play.lower()=='game2'  or play.lower()=='g2':
            new=game()
            new.starting()
            score_from_project=new.score

        else:
            print(colored('\nPlease input l/lyrics, g/game or q/quit \n','red'))
        
    