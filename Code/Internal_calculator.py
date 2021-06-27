# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 14:53:57 2021
Internals Calculator
@author: Qureshi
"""

from tkinter import *
from tkinter import scrolledtext
from PIL import Image,ImageTk
total_quiz_marks = 0
total_assignment_marks = 0
total_sessional1_marks = 0
total_sessional2_marks = 0
quiz_counter = 0
assignment_counter = 0
sessional1_counter = 0
sessional2_counter = 0
window = Tk()

def Quiz():
    global quiz_counter, total_quiz_marks 
    quiz_obtained =  Quiz_obtained_entery_section.get() 
    quiz_out_of =  Quiz_total_entery_section.get()
    quiz_marks = float(quiz_obtained) / float(quiz_out_of)
    quiz_marks = quiz_marks * 15
    if (quiz_counter == 0):
        total_quiz_marks = quiz_marks
        quiz_counter = 2
    elif(quiz_counter == 2):
        total_quiz_marks = (quiz_marks + total_quiz_marks) / quiz_counter
        
    Quiz_total_label.configure(text = total_quiz_marks)
def Assignment():
    global assignment_counter, total_assignment_marks 
    assignment_obtained =  Assignment_obtained_entery_section.get() 
    assignment_out_of =  Assignment_total_entery_section.get()
    assignment_marks = float(assignment_obtained) / float(assignment_out_of)
    assignment_marks = assignment_marks * 10
    if (assignment_counter == 0):
        total_assignment_marks = assignment_marks
        assignment_counter = 2
    elif(assignment_counter == 2):
        total_assignment_marks = (assignment_marks + total_assignment_marks) / assignment_counter
        
    Assignment_total_label.configure(text = total_assignment_marks)
def Sessional_one():
    global sessional1_counter, total_sessional1_marks 
    sessional1_obtained =  Sessional_one_obtained_entery_section.get() 
    sessional1_out_of =  Sessional_one_total_entery_section.get()
    sessional1_marks = float(sessional1_obtained) / float(sessional1_out_of)
    sessional1_marks = sessional1_marks * 10
    if (sessional1_counter == 0):
        total_sessional1_marks = sessional1_marks
        sessional1_counter = 2
    elif(sessional1_counter == 2):
        total_sessional1_marks = (sessional1_marks + total_sessional1_marks) / sessional1_counter
        
    Sessional_one_total_label.configure(text = total_sessional1_marks)
def Sessional_two():
    global sessional2_counter, total_sessional2_marks 
    sessional2_obtained =  Sessional_two_obtained_entery_section.get() 
    sessional2_out_of =  Sessional_two_total_entery_section.get()
    sessional2_marks = float(sessional2_obtained) / float(sessional2_out_of)
    sessional2_marks = sessional2_marks * 15
    if (sessional2_counter == 0):
        total_sessional2_marks = sessional2_marks
        sessional2_counter = 2
    elif(sessional2_counter == 2):
        total_sessional2_marks = (sessional2_marks + total_sessional2_marks) / sessional2_counter
        
    Sessional_two_total_label.configure(text = total_sessional2_marks)

def Total():
        Total_marks = total_quiz_marks + total_assignment_marks + total_sessional1_marks + total_sessional2_marks
        Total_label.configure(text = Total_marks)

def Reset():
    global total_quiz_marks, total_assignment_marks, total_sessional1_marks, total_sessional2_marks, quiz_counter, assignment_counter, sessional1_counter, sessional2_counter
    total_quiz_marks = 0
    total_assignment_marks = 0
    total_sessional1_marks = 0
    total_sessional2_marks = 0
    quiz_counter = 0
    assignment_counter = 0
    sessional1_counter = 0
    sessional2_counter = 0
    Quiz_total_label.configure(text = '0')
    Assignment_total_label.configure(text = '0')
    Sessional_one_total_label.configure(text = '0')
    Sessional_two_total_label.configure(text = '0')
    Total_label.configure(text = '0')
    
#########################################################################################################################
######################################### GUI Implementation #############################################################    
##########################################################################################################################        
window.title("Internal Marks Calculator app")
window.configure(background = '#23272a')
#window.geometry('1280x900')

################### Main Labels #############################
title_lable = Label(window, text = 'Internal Marks Calculator', font=("Arial Bold", 30), bg = '#23272a', fg = 'white')
title_lable.grid(column =1 , row =1 )

email_lable = Label(window, text ='cntct_me: asgharaliq99@gmail.com', font=("Arial Bold", 15), bg = '#23272a', fg = 'white' )
email_lable.grid(column =5 , row =1 )

section1_divider_label = Label(window, text = '-----------', font=("Arial Bold", 20), bg = '#23272a', fg = '#23272a')
section1_divider_label.grid(column =3 , row =2)
############## Quiz Section ####################################
Quiz_tag_lable = Label(window, text = 'Quiz Section', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Quiz_tag_lable.grid(column =1 , row =3)

Quiz_obtained_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Quiz_obtained_entery_section.grid(column = 1, row = 4)

Quiz_out_of_label = Label(window, text = '/', font=("Arial Bold", 30), bg = '#23272a', fg = 'white')
Quiz_out_of_label.grid(column = 2, row = 4)

Quiz_total_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Quiz_total_entery_section.grid(column = 3, row = 4)

Quiz_enter_button = Button(window, text = 'Enter', font=("Arial Bold", 20), bg = '#2c2f33', fg = 'white', command = Quiz)
Quiz_enter_button.grid(column = 4, row = 4)

Quiz_total_label = Label(window, text = '0', font=("Arial Bold", 25), bg = '#23272a', fg = 'white')
Quiz_total_label.grid(column = 5, row = 4)

Quiz_obtained_tag = Label(window, text = 'Obtained', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Quiz_obtained_tag.grid(column = 1, row = 5)

Quiz_out_of_tag = Label(window, text = 'Out of', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Quiz_out_of_tag.grid(column = 3, row = 5)

Quiz_total_tag = Label(window, text = 'TOTAL 15% weightage', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Quiz_total_tag.grid(column = 5, row = 5)
##############################################################################
section2_divider_label = Label(window, text = '-----------', font=("Arial Bold", 20), bg = '#23272a', fg = '#23272a')
section2_divider_label.grid(column =3 , row =6)
############## ASSIGNMENT Section ####################################
Assignment_tag_lable = Label(window, text = 'Assignment Section', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Assignment_tag_lable.grid(column =1 , row =7)

Assignment_obtained_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Assignment_obtained_entery_section.grid(column = 1, row = 8)

Assignment_out_of_label = Label(window, text = '/', font=("Arial Bold", 30), bg = '#23272a', fg = 'white')
Assignment_out_of_label.grid(column = 2, row = 8)

Assignment_total_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Assignment_total_entery_section.grid(column = 3, row = 8)

Assignment_enter_button = Button(window, text = 'Enter', font=("Arial Bold", 20), bg = '#2c2f33', fg = 'white', command = Assignment)
Assignment_enter_button.grid(column = 4, row = 8)

Assignment_total_label = Label(window, text = '0', font=("Arial Bold", 25), bg = '#23272a', fg = 'white')
Assignment_total_label.grid(column = 5, row = 8)

Assignment_obtained_tag = Label(window, text = 'Obtained', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Assignment_obtained_tag.grid(column = 1, row = 9)

Assignment_out_of_tag = Label(window, text = 'Out of', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Assignment_out_of_tag.grid(column = 3, row = 9)

Assignment_total_tag = Label(window, text = 'TOTAL 10% weightage', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Assignment_total_tag.grid(column = 5, row = 9)
##############################################################################
section3_divider_label = Label(window, text = '-----------', font=("Arial Bold", 20), bg = '#23272a', fg = '#23272a')
section3_divider_label.grid(column =3 , row =10)
############## SESSIONAL 1 Section ####################################
Sessional_one_tag_lable = Label(window, text = 'Sessional 1 Section', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_one_tag_lable.grid(column =1 , row =11)

Sessional_one_obtained_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Sessional_one_obtained_entery_section.grid(column = 1, row = 12)

Sessional_one_out_of_label = Label(window, text = '/', font=("Arial Bold", 30), bg = '#23272a', fg = 'white')
Sessional_one_out_of_label.grid(column = 2, row = 12)

Sessional_one_total_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Sessional_one_total_entery_section.grid(column = 3, row = 12)

Sessional_one_enter_button = Button(window, text = 'Enter', font=("Arial Bold", 20), bg = '#2c2f33', fg = 'white', command = Sessional_one)
Sessional_one_enter_button.grid(column = 4, row = 12)

Sessional_one_total_label = Label(window, text = '0', font=("Arial Bold", 25), bg = '#23272a', fg = 'white')
Sessional_one_total_label.grid(column = 5, row = 12)

Sessional_one_obtained_tag = Label(window, text = 'Obtained', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_one_obtained_tag.grid(column = 1, row = 13)

Sessional_one_out_of_tag = Label(window, text = 'Out of', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_one_out_of_tag.grid(column = 3, row = 13)

Sessional_one_total_tag = Label(window, text = 'TOTAL 10% weightage', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_one_total_tag.grid(column = 5, row = 13)
##############################################################################
section4_divider_label = Label(window, text = '-----------', font=("Arial Bold", 20), bg = '#23272a', fg = '#23272a')
section4_divider_label.grid(column =3 , row =14)
############## SESSIONAL 2 Section ####################################
Sessional_two_tag_lable = Label(window, text = 'Sessional 2 Section', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_two_tag_lable.grid(column =1 , row =15)

Sessional_two_obtained_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Sessional_two_obtained_entery_section.grid(column = 1, row = 16)

Sessional_two_out_of_label = Label(window, text = '/', font=("Arial Bold", 30), bg = '#23272a', fg = 'white')
Sessional_two_out_of_label.grid(column = 2, row = 16)

Sessional_two_total_entery_section = Entry(window, width = 20, bg = '#2c2f33', fg = 'white')
Sessional_two_total_entery_section.grid(column = 3, row = 16)

Sessional_two_enter_button = Button(window, text = 'Enter', font=("Arial Bold", 20), bg = '#2c2f33', fg = 'white', command = Sessional_two)
Sessional_two_enter_button.grid(column = 4, row = 16)

Sessional_two_total_label = Label(window, text = '0', font=("Arial Bold", 25), bg = '#23272a', fg = 'white')
Sessional_two_total_label.grid(column = 5, row = 16)

Sessional_two_obtained_tag = Label(window, text = 'Obtained', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_two_obtained_tag.grid(column = 1, row = 17)

Sessional_two_out_of_tag = Label(window, text = 'Out of', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_two_out_of_tag.grid(column = 3, row = 17)

Sessional_two_total_tag = Label(window, text = 'TOTAL 15% weightage', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Sessional_two_total_tag.grid(column = 5, row = 17)
##############################################################################
section5_divider_label = Label(window, text = '-----------', font=("Arial Bold", 20), bg = '#23272a', fg = '#23272a')
section5_divider_label.grid(column =3 , row =18)
############## TOTAL Section ####################################
Total_tag_lable = Label(window, text = 'Total Internal Marks', font=("Arial Bold", 20), bg = '#23272a', fg = 'white')
Total_tag_lable.grid(column =1 , row =19)

Total_enter_button = Button(window, text = 'Press to Total', font=("Arial Bold", 20), bg = '#2c2f33', fg = 'white', command = Total)
Total_enter_button.grid(column = 3, row = 19)

Total_label = Label(window, text = '0', font=("Arial Bold", 25), bg = '#23272a', fg = 'white')
Total_label.grid(column = 5, row = 19)

##############################################################################
section6_divider_label = Label(window, text = '-----------', font=("Arial Bold", 20), bg = '#23272a', fg = '#23272a')
section6_divider_label.grid(column =3 , row =20)

Reset_button = Button(window, text = 'Reset Marks', font=("Arial Bold", 20), bg = '#2c2f33', fg = 'white', command = Reset)
Reset_button.grid(column = 3, row = 21)

section7_divider_label = Label(window, text = '-----------', font=("Arial Bold", 20), bg = '#23272a', fg = '#23272a')
section7_divider_label.grid(column =3 , row =22)

window.mainloop() 