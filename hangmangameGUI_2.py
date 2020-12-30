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
This class generates the game interface and the drawing screen.
Zhibo Wang and Manisha Bhowmik worked on this GUI class collaboratively
'''
'''
Analysis
HangmangameGUI_2
Output:
  --a string showing what letters are guessed correctly by the user
  --status of the game (whether the user lost or won the game)
  --Drawing of hangman or part of hangman
Tasks:
  1. Create GUI with (Note that all names given are assumed to begin with
     self.__)
     --Model--
       --country(Country)
     --Controllers--
       --from button_A to button_Z and button_space (Button objects)
       --again_button and quit_button
     --View--
       --output_string (str containing the information on what characters
                        and the position of the characters)
       --status_string (str showing whether the user lost or won the game)
  2. Event handlers
     --get_hint(self)
     --from get_letter_A(self) to get_letter_Z(self),
       get_letter_space(self)
     --show_or_draw(self,letter)
     --play_again(self),close_all(self)
'''

from country import *
from tkinter import *


class HangmangameGUI_2:

  def __init__(self):

    #Set the window and add window title
    self.__window = Tk()
    self.__window.title('Play Hangman - Country Names')
    self.__window['padx'] = 20
    self.__window['pady'] = 20
    self.__window['bg'] = 'lightblue'

    #Set the model
    self.__country = Country()
    self.__country.draw_initially()

    #Set frame1 to display 'Guess letters to fill in the blank!'
    self.__frame1 = Frame(self.__window)
    self.__frame1.grid(row=1)
    self.__title_label = Label(self.__frame1, \
       text='Guess letters to fill in the blank!',\
                               bg='lightgreen',fg='black',\
       font =('Times', '14', 'bold'))
    self.__title_label.grid(row=1)

    #Set frame2, the dynamic label to show how many characters there are
    #in the country name and what characters are guessed right by the user
    self.__frame2 = Frame(self.__window)
    self.__frame2.grid(row=2)
    
    self.__output_string = StringVar()
    self.__output_string.set(self.get_hint())
    self.__show_label = Label(self.__frame2, \
        textvariable=self.__output_string, bg='lightblue',fg='purple', \
        font=('Times', '24', 'bold'))
    self.__show_label.grid(row=1)

    #Set frame3 and the buttons for upper letters from A to I
    self.__frame3 = Frame(self.__window)
    self.__frame3.grid(row=3)
    self.__button_A = Button(self.__frame3, text ='A',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_A)
    self.__button_A.grid(row=1,column=1)
    self.__button_B = Button(self.__frame3, text ='B',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_B)
    self.__button_B.grid(row=1,column=2)
    self.__button_C = Button(self.__frame3, text ='C',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_C)
    self.__button_C.grid(row=1,column=3)
    self.__button_D = Button(self.__frame3, text ='D',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_D)
    self.__button_D.grid(row=1,column=4)
    self.__button_E = Button(self.__frame3, text ='E',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_E)
    self.__button_E.grid(row=1,column=5)
    self.__button_F = Button(self.__frame3, text ='F',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_F)
    self.__button_F.grid(row=1,column=6)
    self.__button_G = Button(self.__frame3, text ='G',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_G)
    self.__button_G.grid(row=1,column=7)
    self.__button_H = Button(self.__frame3, text ='H',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_H)
    self.__button_H.grid(row=1,column=8)
    self.__button_I = Button(self.__frame3, text ='I',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_I)
    self.__button_I.grid(row=1,column=9)

    #Set frame4 and the buttons for upper letters from J to R
    self.__frame4 = Frame(self.__window)
    self.__frame4.grid(row=4)
    self.__button_J = Button(self.__frame4, text ='J',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_J)
    self.__button_J.grid(row=1,column=1)
    self.__button_K = Button(self.__frame4, text ='K',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_K)
    self.__button_K.grid(row=1,column=2)
    self.__button_L = Button(self.__frame4, text ='L',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_L)
    self.__button_L.grid(row=1,column=3)
    self.__button_M = Button(self.__frame4, text ='M',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_M)
    self.__button_M.grid(row=1,column=4)
    self.__button_N = Button(self.__frame4, text ='N',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_N)
    self.__button_N.grid(row=1,column=5)
    self.__button_O = Button(self.__frame4, text ='O',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_O)
    self.__button_O.grid(row=1,column=6)
    self.__button_P = Button(self.__frame4, text ='P',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_P)
    self.__button_P.grid(row=1,column=7)
    self.__button_Q = Button(self.__frame4, text ='Q',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_Q)
    self.__button_Q.grid(row=1,column=8)
    self.__button_R = Button(self.__frame4, text ='R',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_R)
    self.__button_R.grid(row=1,column=9)

    #Set frame5 and the buttons for the upper letters from S to Z and the space button
    self.__frame5 = Frame(self.__window)
    self.__frame5.grid(row=5)
    self.__button_S = Button(self.__frame5, text ='S',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_S)
    self.__button_S.grid(row=1,column=1)
    self.__button_T = Button(self.__frame5, text ='T',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_T)
    self.__button_T.grid(row=1,column=2)
    self.__button_U = Button(self.__frame5, text ='U',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_U)
    self.__button_U.grid(row=1,column=3)
    self.__button_V = Button(self.__frame5, text ='V',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_V)
    self.__button_V.grid(row=1,column=4)
    self.__button_W = Button(self.__frame5, text ='W',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_W)
    self.__button_W.grid(row=1,column=5)
    self.__button_X = Button(self.__frame5, text ='X',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_X)
    self.__button_X.grid(row=1,column=6)
    self.__button_Y = Button(self.__frame5, text ='Y',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_Y)
    self.__button_Y.grid(row=1,column=7)
    self.__button_Z = Button(self.__frame5, text ='Z',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_Z)
    self.__button_Z.grid(row=1,column=8)
    self.__button_space = Button(self.__frame5, text =' ',bg='white',fg='black',\
          font=('Times', '12', 'bold'), command=self.get_letter_space)
    self.__button_space.grid(row=1,column=9)

    #Set frame6 and the dynamic label to show final status
    self.__frame6 = Frame(self.__window)
    self.__frame6.grid(row=6)

    self.__status_string = StringVar()
    self.__status_string.set('')
    self.__status_label = Label(self.__frame6, textvariable=self.__status_string,\
                     bg='lightblue',fg='red', font=('Times', '18', 'bold'))
    self.__status_label.grid(row=1)

    #Set frame7, play again button and quit button
    self.__frame7 = Frame(self.__window, bg='lightblue')
    self.__frame7.grid(row=7)
    self.__again_button = Button(self.__frame7, text='PLAY AGAIN', bg = 'orange',\
                       fg='black', font=('Times', '12', 'bold'),\
                       command=self.play_again)
    self.__again_button.grid(row=1,column=1,padx=10)
    self.__quit_button = Button(self.__frame7, text='  QUIT  ', bg = 'orange',\
                       fg='black', font=('Times', '12', 'bold'),\
                       command=self.close_all)
    self.__quit_button.grid(row=1,column=3)
    
    # run listener
    mainloop()
                    
  #----------------Define event handlers----------------------------------
  #returns the lenghth of the country name
  #invokes: get_country_name_length()(Country)
  def get_hint(self):
    return self.__country.get_country_name_length()
                            
  # If a single button is pressed, show_or_draw() will be revoked and
  # the button disappears from the window
  # invokes: show_or_draw()
  def get_letter_A(self):
    self.show_or_draw('A')
    self.__button_A.destroy()

  def get_letter_B(self):
    self.show_or_draw('B')
    self.__button_B.destroy()
    
  def get_letter_C(self):
    self.show_or_draw('C')
    self.__button_C.destroy()

  def get_letter_D(self):
    self.show_or_draw('D')
    self.__button_D.destroy()

  def get_letter_E(self):
    self.show_or_draw('E')
    self.__button_E.destroy()

  def get_letter_F(self):
    self.show_or_draw('F')
    self.__button_F.destroy()

  def get_letter_G(self):
    self.show_or_draw('G')
    self.__button_G.destroy()

  def get_letter_H(self):
    self.show_or_draw('H')
    self.__button_H.destroy()

  def get_letter_I(self):
    self.show_or_draw('I')
    self.__button_I.destroy()

  def get_letter_J(self):
    self.show_or_draw('J')
    self.__button_J.destroy()

  def get_letter_K(self):
    self.show_or_draw('K')
    self.__button_K.destroy()

  def get_letter_L(self):
    self.show_or_draw('L')
    self.__button_L.destroy()

  def get_letter_M(self):
    self.show_or_draw('M')
    self.__button_M.destroy()

  def get_letter_N(self):
    self.show_or_draw('N')
    self.__button_N.destroy()

  def get_letter_O(self):
    self.show_or_draw('O')
    self.__button_O.destroy()

  def get_letter_P(self):
    self.show_or_draw('P')
    self.__button_P.destroy()

  def get_letter_Q(self):
    self.show_or_draw('Q')
    self.__button_Q.destroy()

  def get_letter_R(self):
    self.show_or_draw('R')
    self.__button_R.destroy()

  def get_letter_S(self):
    self.show_or_draw('S')
    self.__button_S.destroy()

  def get_letter_T(self):
    self.show_or_draw('T')
    self.__button_T.destroy()

  def get_letter_U(self):
    self.show_or_draw('U')
    self.__button_U.destroy()

  def get_letter_V(self):
    self.show_or_draw('V')
    self.__button_V.destroy()

  def get_letter_W(self):
    self.show_or_draw('W')
    self.__button_W.destroy()

  def get_letter_X(self):
    self.show_or_draw('X')
    self.__button_X.destroy()

  def get_letter_Y(self):
    self.show_or_draw('Y')
    self.__button_Y.destroy()

  def get_letter_Z(self):
    self.show_or_draw('Z')
    self.__button_Z.destroy()

  def get_letter_space(self):
    self.show_or_draw(' ')
    self.__button_space.destroy()

  #Params: letter(str)
  #invokes: two_conditions()(Country), get_country_list()(Country),
  #         show_a_letter()(Country),turtletime_increment()(Country),
  #         draw_hangman()(Country)
  def show_or_draw(self, letter):
    if self.__country.two_conditions():
      if letter in (self.__country.get_country_list()):
        while letter in self.__country.get_country_list():
          self.__country.show_a_letter(letter)
          self.__status_string.set(self.__country.get_final_status()) 
      else:
        self.__country.turtletime_increment()
        self.__country.draw_hangman()
        self.__status_string.set(self.__country.get_final_status())
      self.__output_string.set(self.__country.get_temp_country_name())

  #Close current interface and clear the drawing on the turtle screen
  #invoke HangmangameGUI_2()
  #invokes: clear_win()(Country)
  def play_again(self):
    self.__window.destroy()
    self.__country.clear_win()
    HangmangameGUI_2()

  #Close current interface and the turtle screen
  def close_all(self):
    self.__window.destroy()
    self.__country.close_win()
    
    

##HangmangameGUI_2()

