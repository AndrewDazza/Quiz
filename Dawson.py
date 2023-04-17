import tkinter as Tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mb
import json

root = Tk()
root.title("Dawson Quiz")
root.iconbitmap(r"C:\Users\Andrew\Downloads\Dawson_icon.ico")
root.geometry("1200x800")


#Main Page

bg = ImageTk.PhotoImage(Image.open(r"C:\Users\Andrew\Downloads\Dawson_s_Creek_Intro_Screen.0.jfif"))
my_label1 = Label(root, image=bg)
my_label1.place(x=0, y=0)

 
class myQuiz:  
   
    def __init__(self):       
        self.quesNumber = 0  
  
        self.displayTitle()  
        self.displayQuestion()  
            
        self.optSelected = IntVar()  
           
        self.options = self.radioButtons()  
           
        # displaying the options for the current question  
        self.displayOptions()  
           
        # displaying the button for next and exit.  
        self.buttons()  
           
        # number of questions  
        self.dataSize = len(question)  
           
        # keeping a counter of right answers  
        self.rightAnswer = 0  
  
  
    # results display
        
    def displayResult(self):  
        # calculating the wrong/right count  
        wrongCount = self.dataSize - self.rightAnswer  
        rightAnswer = f"Correct: {self.rightAnswer}"  
        wrongAnswer = f"Wrong: {wrongCount}"  
           
        # calculating the percentage of right answers  
        the_score = int(self.rightAnswer / self.dataSize * 100)  
        the_result = f"Score: {the_score}%" 

        if the_score >= 80:
        
            # showing a message box to display the result  
            mb.showinfo("Wow you're such a creek geek!", f"{the_result} \n{rightAnswer} \n{wrongAnswer}")  

        else:
            #pop up the crying dawson pic    
            popup = Toplevel()
            popup.title("Crying Dawson")
            popup.geometry("800x800")

            # Load the image using PIL
            image = Image.open(r"C:\Users\Andrew\Desktop\Python Learning\Dawson pics\dawson_cry.jpg")
            image = image.resize((200, 200), Image.LANCZOS)  # Resize the image to fit the popup
            photo = ImageTk.PhotoImage(image)

            # Create a label with the image as the background
            label = Label(popup, image=photo)
            label.image = photo  # Keep a reference to the image to prevent garbage collection
            label.place(x=0, y=0)

            # Add a message to the label
            message = "Seems like you're not a Creek Geek after all!", f"{the_result} \n{rightAnswer} \n{wrongAnswer}"
            message_label = Label(label, text=message, font=("Arial", 12), bg="#FFFFFF")
            message_label.pack(pady=10)

            # Add a button to close the popup
            close_button = Button(label, text="Close", command=popup.destroy)
            close_button.pack(pady=10)

            label.pack()
            popup.mainloop()
  
     
    def checkAnswer(self, quesNumber):  
        # checking for if the selected option is right  
        if self.optSelected.get() == answer[quesNumber]: 
            mb.showinfo("correct!", "You got it!") 
            # if the option is right it return true  
            return True  
  
     
    def nextButton(self):  
        # Checking whether the answer is correct  
        if self.checkAnswer(self.quesNumber):  
            # if the answer is correct it increments the correct by 1  
            self.rightAnswer += 1
        else:
            mb.showinfo("WRONG!!!!", "You fuckin SUUUCKKK!!!")    
               
           
        # Moving to next Question by incrementing the quesNumber counter  
        self.quesNumber += 1  
           
        # checking whether the quesNumber size is equal to the data size  
        if self.quesNumber == self.dataSize:   
            # if it is correct then it displays the score  
            self.displayResult()  
              
            # destroying the GUI  
            root.destroy()  
        else:  
            # showing the next question  
            self.displayQuestion()  
            self.displayOptions()  
  
 
    def buttons(self):  
          
        # The first button is the Next button  
        # to move to the next Question  
        next_button = Button(  
            root,  
            text = "Next",  
            command = self.nextButton,  
            width = 10,  
            bg = "blue",  
            fg = "white",  
            font = ("ariel", 16, "bold")  
            )  
           
        # placing the button on the screen  
        next_button.place(x = 500, y = 700)  
           
        # The second button is the quit button  
        # which is used to Quit the GUI  
        quit_button = Button(  
            root,  
            text = "Quit",  
            command = root.destroy,  
            width = 5,  
            bg = "black",  
            fg = "white",  
            font = ("ariel", 16, " bold")  
            )  
           
        # placing the Quit button on the screen  
        quit_button.place(x = 1100, y = 50)  
  

    def displayOptions(self):  
        val = 0  
        # deselecting the options  
        self.optSelected.set(0)  
        # looping over the options to be displayed  
        # for the text of the radio buttons.  
        for opt in opts[self.quesNumber]:  
            self.options[val]['text'] = opt  
            val += 1  
  
  
    def displayQuestion(self):  
           
        # setting the Question properties  
        quesNumber = Label(  
            root,  
            text = question[self.quesNumber],  
            width = 75,  
            font = ('ariel', 16, 'bold'),  
            anchor = 'w'  
            )  
           
        # placing the option on the screen  
        quesNumber.place(x = 70, y = 100)  
      
   
    def displayTitle(self):           
        # The title to be shown  
        myTitle = Label(  
            root,  
            text = "ULTIMATE DAWSON FAN QUIZ!!!",  
            width = 75,  
            bg = "blue",  
            fg = "white",  
            font = ("ariel", 20, "bold")  
            )  
          
        # placing the title  
        myTitle.place(x = 0, y = 2)  
   
   
    def radioButtons(self):  
           
        # initializing the list with an empty list of options  
        qList = []  
           
        # position of the first option  
        y_pos = 150  
           
        # adding the options to the list  
        while len(qList) < 4:  
               
            # setting the radio button properties  
            radio_button = Radiobutton(  
                root,  
                text = " ",  
                variable = self.optSelected,  
                value = len(qList) + 1,  
                font = ("ariel", 14)  
                )  
              
            # adding the button to the list  
            qList.append(radio_button)  
               
            # placing the button  
            radio_button.place(x = 100, y = y_pos)  
               
            # incrementing the y-axis position by 40  
            y_pos += 40  
           
        # returning the radio buttons  
        return qList  
  
# getting the data from the json file  
with open('data.json') as json_file:  
    data = json.load(json_file)  
   
# setting the question, options, and answer  
question = (data['ques'])  
opts = (data['choices'])  
answer = (data[ 'ans'])  
   

quiz = myQuiz()  
  
    
root.mainloop()