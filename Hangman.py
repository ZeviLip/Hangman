
import tkinter
from tkinter import *
from tkinter import messagebox

## Creates window and it's properties as well as establishes number of chances ##
window = Tk()
window.title("Hangman")
window.geometry("1100x320+100+300")
window.lift()
window.attributes('-topmost',True)
window.after_idle(window.attributes,'-topmost',False)
chances=5;

## Creates entries and labels them using grid pattern connected to buttons ##
v1 = StringVar()
entry = Entry (window,fg = 'white', borderwidth = 6)
entry.grid(row = 4)
label_e = Label(window, text = 'Type your word: ')
label_e.grid(row = 3)
entry2 = Entry (window,  fg = 'black', borderwidth = 6)
entry2.grid(row = 2)
label_e = Label(window, text = 'How many letters is your word? (up to 16 then press enter to start): ')
label_e.grid(row = 1)


hanger=['''
                 _____
                |     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \   _|_''','''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    
                
                    \O/      
          ~WINNER~   |   ~WINNER~        
                     |    
                    / \ 
                                       
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']
hangman_img = Label(window, textvariable = v1)
v1.set(hanger[0])
hangman_img.grid(row = 0, padx = 0, pady = 0)


## Creates lank spaced buttons that will be configured if user guesses correct lettter ##

btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn05 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn06 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn07 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn08 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn09 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn010 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn011 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn012 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn013 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn014 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn015 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn016 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn017 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn018 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))

## Takes Entry2 input that establishes number of characters in user's word and makes that amount of butttons (using grid pattern) ##
def lose():
    if entry2.get() == '1':
        btn01.grid(column=2, row=0)
    if entry2.get() == '2':
        btn01.grid(column=2, row=0)
        btn02.grid(column=3, row=0)
    if entry2.get() == '3':
        btn01.grid(column=2, row=0)
        btn02.grid(column=3, row=0)
        btn03.grid(column=4, row=0)
    if entry2.get() == '4':
        btn01.grid(column=2, row=0)
        btn02.grid(column=3, row=0)
        btn03.grid(column=4, row=0)
        btn04.grid(column=5, row=0)
    if entry2.get() == '5':
        btn01.grid(column=2, row=0)
        btn02.grid(column=3, row=0)
        btn03.grid(column=4, row=0)
        btn04.grid(column=5, row=0)
        btn05.grid(column=6, row=0)
    if entry2.get() == '6':
        btn01.grid(column=2, row=0)
        btn02.grid(column=3, row=0)
        btn03.grid(column=4, row=0)
        btn04.grid(column=5, row=0)
        btn05.grid(column=6, row=0)
        btn06.grid(column=7, row=0)
    if entry2.get() == '7':
        btn01.grid(column=2, row=0)
        btn02.grid(column=3, row=0)
        btn03.grid(column=4, row=0)
        btn04.grid(column=5, row=0)
        btn05.grid(column=6, row=0)
        btn06.grid(column=7, row=0)
        btn07.grid(column=8, row=0)
    if entry2.get() == '8':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
    if entry2.get() == '9':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
    if entry2.get() == '10':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
        btn010.grid(column=10, row=0)
    if entry2.get() == '11':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
        btn010.grid(column=10, row=0)
        btn011.grid(column=11, row=0)
    if entry2.get() == '12':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
        btn010.grid(column=10, row=0)
        btn011.grid(column=11, row=0)
        btn012.grid(column=12, row=0)
    if entry2.get() == '13':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
        btn010.grid(column=10, row=0)
        btn011.grid(column=11, row=0)
        btn012.grid(column=12, row=0)
        btn013.grid(column=13, row=0)
    if entry2.get() == '14':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
        btn010.grid(column=10, row=0)
        btn011.grid(column=11, row=0)
        btn012.grid(column=12, row=0)
        btn013.grid(column=13, row=0)
        btn014.grid(column=14, row=0)
    if entry2.get() == '15':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
        btn010.grid(column=10, row=0)
        btn011.grid(column=11, row=0)
        btn012.grid(column=12, row=0)
        btn013.grid(column=13, row=0)
        btn014.grid(column=14, row=0)
        btn015.grid(column=15, row=0)
    if entry2.get() == '16':
        btn01.grid(column=1, row=0)
        btn02.grid(column=2, row=0)
        btn03.grid(column=3, row=0)
        btn04.grid(column=4, row=0)
        btn05.grid(column=5, row=0)
        btn06.grid(column=6, row=0)
        btn07.grid(column=7, row=0)
        btn08.grid(column=8, row=0)
        btn09.grid(column=9, row=0)
        btn010.grid(column=10, row=0)
        btn011.grid(column=11, row=0)
        btn012.grid(column=12, row=0)
        btn013.grid(column=13, row=0)
        btn014.grid(column=14, row=0)
        btn015.grid(column=15, row=0)
        btn016.grid(column=16, row=0)
        
## Binds the lose function to keyboard ##   
def return_lose(event):
    lose()
    
## Game Function
def clicked(alphabet):
    ## globalizes chances and makes the users input the answer/word for hangman (lose() ensures that the correct amount of buttons appear for each letter of the user's input) ##
    global chances
    x1 = str(entry.get())
    x2 = x1.upper()
    answer = list(str(x2))
    lose()
    ## checks whether the alphabet is there in the answer, replaces unmarked buttons with correctly guessed letters as the text ## 
    if alphabet in answer: 
        if entry2.get() == '1':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
        if entry2.get() == '2':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
        if entry2.get() == '3':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
        if entry2.get() == '4':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
        if entry2.get() == '5':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
        if entry2.get() == '6':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
        if entry2.get() == '7':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
        if entry2.get() == '8':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
        if entry2.get() == '9':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
        if entry2.get() == '10':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
            if alphabet==answer[9]:
                btn010["text"] = answer[9];
        if entry2.get() == '11':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
            if alphabet==answer[9]:
                btn010["text"] = answer[9];
            if alphabet==answer[10]:
                btn011["text"] = answer[10];
        if entry2.get() == '12':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
            if alphabet==answer[9]:
                btn010["text"] = answer[9];
            if alphabet==answer[10]:
                btn011["text"] = answer[10];
            if alphabet==answer[11]:
                btn012["text"] = answer[11];
        if entry2.get() == '13':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
            if alphabet==answer[9]:
                btn010["text"] = answer[9];
            if alphabet==answer[10]:
                btn011["text"] = answer[10];
            if alphabet==answer[11]:
                btn012["text"] = answer[11];
            if alphabet==answer[12]:
                btn013["text"] = answer[12];
        if entry2.get() == '14':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
            if alphabet==answer[9]:
                btn010["text"] = answer[9];
            if alphabet==answer[10]:
                btn011["text"] = answer[10];
            if alphabet==answer[11]:
                btn012["text"] = answer[11];
            if alphabet==answer[12]:
                btn013["text"] = answer[12];
            if alphabet==answer[13]:
                btn014["text"] = answer[13];
        if entry2.get() == '15':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
            if alphabet==answer[9]:
                btn010["text"] = answer[9];
            if alphabet==answer[10]:
                btn011["text"] = answer[10];
            if alphabet==answer[11]:
                btn012["text"] = answer[11];
            if alphabet==answer[12]:
                btn013["text"] = answer[12];
            if alphabet==answer[13]:
                btn014["text"] = answer[13];
            if alphabet==answer[14]:
                btn015["text"] = answer[14];
        if entry2.get() == '16':
            if alphabet==answer[0]:
                btn01["text"] = answer[0];
            if alphabet==answer[1]:
                btn02["text"] = answer[1];
            if alphabet==answer[2]:
                btn03["text"] = answer[2];
            if alphabet==answer[3]:
                btn04["text"] = answer[3];
            if alphabet==answer[4]:
                btn05["text"] = answer[4];
            if alphabet==answer[5]:
                btn06["text"] = answer[5];
            if alphabet==answer[6]:
                btn07["text"] = answer[6];
            if alphabet==answer[7]:
                btn08["text"] = answer[7];
            if alphabet==answer[8]:
                btn09["text"] = answer[8];
            if alphabet==answer[9]:
                btn010["text"] = answer[9];
            if alphabet==answer[10]:
                btn011["text"] = answer[10];
            if alphabet==answer[11]:
                btn012["text"] = answer[11];
            if alphabet==answer[12]:
                btn013["text"] = answer[12];
            if alphabet==answer[13]:
                btn014["text"] = answer[13];
            if alphabet==answer[14]:
                btn015["text"] = answer[14];
            if alphabet==answer[15]:
                btn016["text"] = answer[15];
    else:
        ## displays chances remaining if user guesses incorrectly and if all chances are used displays a messagebox for loser ##
        txt="Chances remaining "+str(chances);
        label1.configure(text=txt)
        chances = chances - 1;
        if chances<0:
            messagebox.showinfo("GAME OVER","Hanged!!!!!\n the words was: " + str(entry.get()))
            window.destroy()
    if chances == 5:
        v1.set(hanger[1])
    if chances == 4:
        v1.set(hanger[2])
    if chances == 3:
        v1.set(hanger[3])
    if chances == 2:
        v1.set(hanger[4])
    if chances == 1:
        v1.set(hanger[5])
    if chances == 0:
        v1.set(hanger[6])
    ## displays win messagebox for when the game is won under scenarios of different lengths of words ##
    if entry2.get() == '1':
        if btn01["text"]==answer[0]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '2':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '3':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '4':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '5':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '6':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '7':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5]and btn07["text"]==answer[6]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '8':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '9':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '10':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8] and btn010["text"]==answer[9]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '11':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8] and btn010["text"]==answer[9] and btn011["text"]==answer[10]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '12':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8] and btn010["text"]==answer[9]   and btn011["text"]==answer[10] and btn012["text"]==answer[11]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '13':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2]  and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8] and btn010["text"]==answer[9] and btn011["text"]==answer[10] and btn012["text"]==answer[11] and btn013["text"]==answer[12]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '14':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8] and btn010["text"]==answer[9] and btn011["text"]==answer[10] and btn012["text"]==answer[11] and btn013["text"]==answer[12] and btn014["text"]==answer[13]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '15':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8] and btn010["text"]==answer[9] and btn011["text"]==answer[10] and btn012["text"]==answer[11] and btn013["text"]==answer[12] and btn014["text"]==answer[13] and btn015["text"]==answer[14]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    if entry2.get() == '16':
        if btn01["text"]==answer[0] and btn02["text"]==answer[1] and btn03["text"]==answer[2] and btn04["text"]==answer[3] and btn05["text"]==answer[4] and btn06["text"]==answer[5] and btn07["text"]==answer[6] and btn08["text"]==answer[7] and btn09["text"]==answer[8] and btn010["text"]==answer[9] and btn011["text"]==answer[10] and btn012["text"]==answer[11] and btn013["text"]==answer[12] and btn014["text"]==answer[13] and btn015["text"]==answer[14] and btn016["text"]==answer[15]:
            messagebox.showinfo("congratulations", "YOU WON HANGMAN!!!!")
            v1.set(hanger[6])
            window.destroy()
    
    
    

entry2.bind('<Return>', return_lose)


btn1 = Button(window, text="A",bg="skyblue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
btn1.grid(column=1, row=1)
btn2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
btn2.grid(column=2, row=1)
btn3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
btn3.grid(column=3, row=1)
btn4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
btn4.grid(column=4, row=1)
btn5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
btn5.grid(column=5, row=1)
btn6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
btn6.grid(column=6, row=1)
btn7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
btn7.grid(column=7, row=1)
btn8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
btn8.grid(column=8, row=1)

btn9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
btn9.grid(column=2, row=2)
btn10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
btn10.grid(column=3, row=2)
btn11= Button(window, text="K",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
btn11.grid(column=4, row=2)
btn12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
btn12.grid(column=5, row=2)
btn13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
btn13.grid(column=6, row=2)
btn14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn14.grid(column=7, row=2)

btn15= Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
btn15.grid(column=3, row=3)
btn16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
btn16.grid(column=4, row=3)
btn17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
btn17.grid(column=5, row=3)
btn18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
btn18.grid(column=6, row=3)

btn19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
btn19.grid(column=1, row=4)
btn20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn20.grid(column=2, row=4)
btn21= Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
btn21.grid(column=3, row=4)
btn22 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
btn22.grid(column=4, row=4)
btn23 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
btn23.grid(column=5, row=4)
btn24 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
btn24.grid(column=6, row=4)
btn25 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
btn25.grid(column=7, row=4)
btn26 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
btn26.grid(column=8, row=4)

def replay():
    window.destroy()
    import Hangman
    window.open()
    return()
replay = Button(window, text = 'REPLAY', fg = 'red',width=6,height=2,command=replay)
replay.grid(row = 6)
label1=Label(window,text="Total Chances are : 6")
label1.grid(row=5,column=0)
window.mainloop()
