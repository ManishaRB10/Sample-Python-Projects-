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
This class can draw the gallows and every part of a hangman.
Manisha Bhowmik designed and coded this class.
'''
from turtle import *

class Hangman:
  
  DRAW_HEAD = 1
  DRAW_BODY = 2
  DRAW_LEFTARM = 3
  DRAW_RIGHTARM = 4
  DRAW_LEFTLEG = 5
  DRAW_RIGHTLEG = 6

  #----------------------------Constructor-----------------------------------
  #Initialize:
  #self.__win (an instance of Screen)
  #self.__alex (an instance of Turtle)
  def __init__(self):
    self.__win = Screen()
    self.__win.title('Draw Hangman')
    self.__win.setworldcoordinates(-80,-180,280,180)
    self.__alex = Turtle()
    self.__alex.pensize(3)

  # Draw the gallows
  def draw_windowandhanger(self):
    self.__win.bgcolor('lightblue')
    self.__alex.hideturtle()
    self.__alex.penup()
    self.__alex.goto(200,-120)
    self.__alex.pendown()
    self.__alex.left(180)
    self.__alex.forward(200)
    self.__alex.goto(100,-120)
    self.__alex.right(90)
    self.__alex.forward(250)
    self.__alex.right(90)
    self.__alex.forward(60)
    self.__alex.right(90)
    self.__alex.forward(10)
    self.__alex.penup()
    self.__alex.goto(180,100)
    self.__alex.pendown()
    
  # Draw part of a hangman
  # params: turtletime (int)
  def draw_hangman(self, turtletime):
    if turtletime == Hangman.DRAW_HEAD:
      self.__alex.color('black','red')
      self.__alex.begin_fill()
      self.__alex.circle(-20)
      self.__alex.end_fill()
      self.__alex.penup()
    elif turtletime == Hangman.DRAW_BODY:
      self.__alex.goto(160,80)
      self.__alex.pendown()
      self.__alex.forward(75)                 
    elif turtletime == Hangman.DRAW_LEFTARM:
      self.__alex.goto(160,70)
      self.__alex.right(45)
      self.__alex.forward(40)
      self.__alex.goto(160,70)
    elif turtletime == Hangman.DRAW_RIGHTARM:
      self.__alex.left(90)
      self.__alex.forward(40)
      self.__alex.penup()
      self.__alex.goto(160,5)
    elif turtletime == Hangman.DRAW_LEFTLEG:
      self.__alex.pendown()
      self.__alex.right(90)
      self.__alex.forward(40)
      self.__alex.penup()
      self.__alex.goto(160,5)
    elif turtletime == Hangman.DRAW_RIGHTLEG:
      self.__alex.pendown()
      self.__alex.left(90)
      self.__alex.forward(40)

  #Close the window
  def close_window(self):
    self.__win.bye()
    
  #Clear the drawing of a turtle in the screen
  def clear_window(self):
    self.__alex.clear()

  

