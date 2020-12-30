'''
Bhowmik, Manisha
mbhowmi1@binghamton.edu
Lab session C58
CA Jia Yang

Zhibo Wang
zwang233@binghamton.edu
Lab session C60
CA Vladimir Malcevic
'''
'''
This GUI class generates the welcome interface of hangman game with a focus on
country name.
Zhibo Wang designed and coded this GUI class.
'''
'''
Analysis
HangmangameGUI_1
Tasks:
1. Create GUI with (Note that all names given are assumed to begin with
     self.__)
   --Controllers--
     -- CONTINUE button, QUIT button (Button objects)
2. Event handlers
   --call_next(self)
'''

from hangmangameGUI_2 import *
from country import *
from tkinter import *


class HangmangameGUI_1:
  
  def __init__(self):

    #Set the window and add window title
    self.__window = Tk()
    self.__window.title('Play Hangman - Country Names')
    self.__window['padx'] = 50
    self.__window['pady'] = 50
    self.__window['bg'] = 'lightgray'

    #Set frame1 and add the title label
    self.__frame1 = Frame(self.__window, bg='lightgray')
    self.__frame1.grid(row=1)
    self.__title_lable =Label(self.__frame1,\
        text ='Would you Like to Play' +'\nHangman with Country Names?',\
        bg = 'yellow', fg = 'black', font =('Times', '14', 'bold'))
    self.__title_lable.grid(row=1,padx=27,pady=25)

    #Set frame2 and add the World Map image
    self.__frame2 = Frame(self.__window,bg='lightgray')
    self.__frame2.grid(row=2)
    self.__image = PhotoImage(file ='World Map.gif') 
    self.__image_label = Label(self.__frame2, image=self.__image)
    self.__image_label.grid(row=1, padx=37)

    #Set frame3 and add continue and quit button
    self.__frame3 = Frame(self.__window,bg='lightgray')
    self.__frame3.grid(row=3)
    
    self.__no_button = Button(self.__frame3, text ='   QUIT   ', bg = 'orange',\
                       fg='black', font=('Times', '12', 'bold'),\
                       command=self.__window.destroy)
    self.__no_button.grid(row=1,column=2,sticky=W+E,padx=44,pady=25)
    
    self.__yes_button = Button(self.__frame3, text = ' CONTINUE ', bg='orange',\
                      fg='black', font =('Times', '12', 'bold'),\
                      command=self.call_next)
    self.__yes_button.grid(row=1,column=1,sticky=W+E,padx=45, pady=25)
    
    #run listener
    mainloop()

    #Define event handler
    #Close current welcome interface and invoke HangmangameGUI_2
  def call_next(self):
    self.__window.destroy()
    HangmangameGUI_2()
    

HangmangameGUI_1()

    
    


