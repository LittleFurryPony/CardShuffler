#This is a simple program that shugg

import random as IMP_RAN

class Deck_Bulider():
    def __init__(self):
        self.__Deck = []
        self.__Number_Of_Decks = 1
        self.__Jokers = False
        self.__Loop = True
        self.__Commands = {"/exit" : {"Function" : self.Exit, "Limit" : None, "Description" : "Exit the program"},
                           "/help" : {"Function" : self.Help, "Limit" : None, "Description" : "Shows the help menu"},
                           "/create_deck" : {"Function" : self.Create_Deck, "Limit" : 1, "Description" : "Creates a new deck"},
                           "/shuffle_deck" : {"Function" : self.Shuffle_Deck, "Limit" : 1, "Description" : "Shuffles the deck"},
                           "/set_deck_num" : {"Function" : self.Set_Deck_Num, "Limit" : 2, "Description" : "Sets the number of decks"},
                           "/set_deck_amount" : {"Function" : self.Set_Deck_Num, "Limit" : 2, "Description" : "Sets the number of decks"},
                           "/set_jokers" : {"Function" : self.Set_Jokers, "Limit" : 1, "Description" : "Sets the number of jokers"},
                           "/draw_card" : {"Function" : self.Draw_Card, "Limit" : 1, "Description" : "Draws a card from the deck"}
        }
    def Exit(self, Command):
        self.__Loop = False
        print("Exiting the program...")
        #^ Exits the program
    def Help(self, Command):
        print("" , *(f"\n{Command} - {self.__Commands[Command]['Description']}" for Command in self.__Commands))
        #^ Shows the help menu
    def Create_Deck(self, Command):
        self.__Deck = ([f"{rank} of {suit}" for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades'] for rank in ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']] + (['Joker Red', 'Joker Black'] if self.__Jokers else [])) * self.__Number_Of_Decks
        #^ Creates a deck of cards with the specified number of decks and jokers
    def Shuffle_Deck(self, Command):
        IMP_RAN.shuffle(self.__Deck)
        #^ Shuffles the deck of cards
    def Set_Deck_Num(self, Command):
        try:
            self.__Number_Of_Decks = int(Command[1]) #Coverts value to integer
            print("Invalid number of decks, must be greater than 0") if self.__Number_Of_Decks < 1 else None
            #^ If the number of decks is less than 1, it will return an error
            self.__Number_Of_Decks = self.__Number_Of_Decks if self.__Number_Of_Decks > 0 else 1
            #^ If the number of decks is less than 1, it will set it to 1
            print(f"Number of decks set to {self.__Number_Of_Decks}")
        except ValueError:
            print("Invalid number of decks, must be an integer"); return None
        #^ Sets the number of decks to be used
    def Set_Jokers(self, Command):
        self.__Jokers = True if False else False
        print(f"Jokers set to {self.__Jokers}")
        #^ Declairs if jokers are used or not
    def Draw_Card(self, Command):
        if len(self.__Deck) == 0: print("Deck is empty, please create a new deck"); return None
        #^ Checks if the deck is empty
        print(f"You Drew The \033[1m{self.__Deck.pop(0)}\033[0m")
        #^ Draws a card from the deck
    def Format_Command(self, Command):
        if Command == "": return ""
        Split = 1; New_Command = []
        if "§" in Command: print("Invalid command, Command Cannot Contain §"); return None
        #^ Checks if the command contains the § character, § is used to split the command
        if len(Command) == 0: print("Invalid Command, Command Cannot Be Empty"); return ""
        #^ Checks if the command is empty
        for Letter in Command:
            if Letter == " " and Split == 1: New_Command.append("§")
            #^ Splits the command into sections if there is a space
            else: New_Command.append(Letter)
            #^ Adds the letter to the command
            if Letter == "\"" or Letter == "'": Split *= -1
            #^ If the letter is a quote, it will toggle split
        return "".join(New_Command).split("§")
        #^ Formats the user input into a recognizable command
    def Play(self):
        while self.__Loop:
            _input = self.Format_Command(input("Press Enter to draw a card or type '/exit' to quit: "))
            if not _input or _input[0] == "": self.Draw_Card("")
                #^ If the user presses enter, it will draw a card
            else:
                if _input[0] in self.__Commands:
                    if self.__Commands[_input[0]]["Limit"] == None:
                        self.__Commands[_input[0]]["Function"](_input)
                    elif self.__Commands[_input[0]]["Limit"] != None and len(_input) == self.__Commands[_input[0]]["Limit"]:
                        self.__Commands[_input[0]]["Function"](_input)

    def Main(self):
        self.Create_Deck(None)
        self.Shuffle_Deck(None)
        self.Play()


Deck_Bulider().Main()
#^ Main function to run the program
