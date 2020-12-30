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
This class generates a randomly generated country name and
the drawing of a hangman or parts of a hangman.
Zhibo Wang and Manisha Bhowmik worked on this class collaboratively
'''
from random import *
from hangman import *

class Country:
  MAX_TIME = 6
  COUNTRY_LIST = ['AFGHANISTAN','ALBANIA','ALGERIA','ANDORRA',\
                  'ANGOLA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA',\
                  'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN',\
                  'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE',\
                  'BENIN','BHUTAN','BOLIVIA','BOSNIA AND HERZEGOVINA'\
                  'BOTSWANA', 'BRAZIL', 'BRUNEI', 'BULGARIA', 'BURKINA FASO',\
                  'BURMA', 'BURUNDI','CAMBODIA','CAMEROON','CANADA',\
                  'CABO VERDE', 'CENTRAL AFRICAN REPUBLIC','CHAD','CHILE',\
                  'CHINA','COLOMBIA','COMOROS','COSTA RICA', 'CROATIA',\
                  'CUBA', 'CURACAO', 'CYPRUS', 'CZECHIA', 'DENMARK', \
                  'DJIBOUTI', 'DOMINICA', 'DOMINICAN REPUBLIC', 'ECUADOR',\
                  'EGYPT', 'EL SALVADOR', 'ERITREA', 'ESTONIA', 'ESWATINI',\
                  'ETHIOPIA', 'FIJI', 'FINLAND', 'FRANCE', 'GABON',\
                  'GERMANY','GHANA', 'GREECE', 'GRENADA', 'GUATEMALA',\
                  'GUYANA', 'HAITI', 'HONDURAS', 'HONG KONG', 'HUNGARY',\
                  'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND',\
                  'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN',\
                  'KAZAKHSTAN', 'KENYA', 'KIRIBATI', 'NORTH KOREA',\
                  'SOUTH KOREA', 'KOSOVO', 'KUWAIT', 'KYRGYZSTAN','LAOS',\
                  'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA',\
                  'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAU',\
                  'MACEDONIA', 'MADAGASCAR', 'MALAWI', 'MALAYSIA',\
                  'MALDIVES', 'MALI', 'MARSHALL ISLANDS', 'MAURITANIA',\
                  'MAURITIUS', 'MEXICO', 'MICRONESIA', 'MOLDOVA', 'MONACO',\
                  'MONGOLIA', 'MONTENEGRO', 'MOROCCO', 'MOZAMBIQUE',\
                  'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NEW ZEALAND',\
                  'NICARAGUA', 'NIGER', 'NORWAY', 'OMAN', 'PAKISTAN',\
                  'PALAU', 'PANAMA', 'PARAGUAY', 'PERU', 'PHILIPPINES',\
                  'POLAND', 'PORTUGAL', 'QATAR', 'ROMANIA', 'RUSSIA',\
                  'RWANDA', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA',\
                  'SIERRA LEONE', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA',\
                  'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',\
                  'SOUTH SUDAN', 'SPAIN', 'SRI LANKA', 'SUDAN', 'SURINAME',\
                  'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN',\
                  'TANZANIA', 'THAILAND', 'TOGO', 'TONGA',\
                  'TRINIDAD AND TOBAGO', 'TUNISIA', 'TURKEY', 'TURKMENISTAN',\
                  'TUVALU', 'UGANDA', 'UKRAINE', 'UNITED ARAB EMIRATES',\
                  'UNITED KINGDOM', 'UNITED STATES OF AMERICA', 'URUGUAY',\
                  'UZBEKISTAN', 'VENEZUELA', 'VIETNAM', 'YEMEN', 'ZAMBIA',\
                  'ZIMBABWE']
  
  
  #--------------------Constructor-----------------------------------------#
  # intialize:
  #self.__hangman (an instance of Hangman class)
  #self.__country (str, a coutry name randomly generated from Country list)
  #self.__tempword_list(list) to a list with the length of self.__country and
  #                           each element being '-'
  #self.__test_list(list) to a list with the length of self.__country and
  #                       each element being '-'
  #self.__turtletime(int) to 0
  #self.__final_status(str) to a empty string
  #self.__country_list(list) to a list being converted from str self.__country
  #invokes: get_initial_country_list() to generate self.__country_list
  
  def __init__(self):
    self.__hangman = Hangman()
    self.__country = Country.COUNTRY_LIST\
                    [randrange(0,len(Country.COUNTRY_LIST))]
    ##print(self.__country)
    self.__tempword_list = ['-'] * len(self.__country)
    self.__test_list = ['?'] * len(self.__country)
    self.__turtletime = 0
    self.__final_status = ''
    self.__country_list = self.get_initial_country_list()
  #---------------------Predicates-----------------------------------------#
  # returns: Whether the guessing for a country name should continue (True)
  #          or stop (False)
  def two_conditions(self):
    return self.__turtletime < Country.MAX_TIME and \
           self.__country_list != self.__test_list
  
  #---------------------Accessors------------------------------------------#
  # returns: the length of the country name
  def get_country_name_length(self):
    return  '-' * len(self.__country)

  # returns: the initial list converted from the country name
  def get_initial_country_list(self):
    self.__country_list = []
    for i in range(len(self.__country)):
      self.__country_list.append(self.__country[i])
    return self.__country_list
  
  # returns: a list modified from the original country list with elements being replaced
  #          replaced by '?' if the user guesses the correct letters
  def get_country_list(self):
    return self.__country_list

  # returns: a list modified from original tempword list with '-' being replaced
  #          by letters and space which have been guessed correctly by the user
  def get_tempword_list(self):
    return self.__tempword_list

  # returns: how many times the user have guessed wrongly
  def get_turtletime(self):
    return self.__turtletime

  # returns: a string converted from self.__tempword_list
  def get_temp_country_name(self):
    return ''.join(self.__tempword_list)
  
  # returns: a string showing whether the user lost or won the game
  def get_final_status(self):
    self.__set_final_status()
    return self.__final_status

  #---------------------Mutators-------------------------------------------#
  # If letter inputted by the user exists in country name, all the
  # corresponding positions for this letter will be replaced by
  # this letter in self.__tempword_list and '?' in self.__country_list
  # params: letter - a letter input by the user (str). 
  def show_a_letter(self, letter):
    while letter in self.__country_list:
      i = self.__country_list.index(letter)
      self.__tempword_list[i] = letter
      self.__country_list[i] = '?'

  # If the user input a character which does not exist in country name,
  # turtletime will increase 1
  def turtletime_increment(self):
    self.__turtletime += 1
    
  # Draw hangman turtle window and the gallows
  # Invokes: draw_windowandhanger()(Hangman)
  def draw_initially(self):
    self.__hangman.draw_windowandhanger()

  # Draw one part of a hangman given the turtle time
  # invokes: draw_hangman(Hangman)
  def draw_hangman(self):
    self.__hangman.draw_hangman(self.__turtletime)

  # Record the status whether the user lost or won the game
  # If the user lost the game, the name of the country will be displayed
  def __set_final_status(self):
    if self.__turtletime == Country.MAX_TIME:
      self.__final_status = 'YOU LOST!' + \
                            ' The Country Name is: '\
                            + self.__country
    elif self.__country_list == self.__test_list:
      self.__final_status = 'YOU WON!'

  # Close hangman turtle window
  # invokes: close_window(Hangman)
  def close_win(self):
    self.__hangman.close_window()

  # Clear the drawing in hangman window
  # invokes: clear_window(Hangman)
  def clear_win(self):
    self.__hangman.clear_window()
      
   
    
    
    
      
    

