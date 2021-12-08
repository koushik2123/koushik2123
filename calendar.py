from tkinter import *

import calendar

def showCal() :


	new_gui = Tk()
	
	
	new_gui.config(background = "light blue")

	
	new_gui.title("CALENDAR")


	new_gui.geometry("1920x1080")


	fetch_year = int(year_field.get())

	cal_content = calendar.calendar(fetch_year)

	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")

	cal_year.grid(row = 4, column = 1, padx = 20)
	
	
	new_gui.mainloop()

	

if __name__ == "__main__" :
    
	gui = Tk()
	
	gui.config(background = "light yellow")

	
	gui.title("CALENDAR")

	gui.geometry("550x600")

	
	cal = Label(gui, text = " CALENDAR for the Year", bg = "light blue",
						font = ("calibri", '40', 'bold','italic','underline'))

	
	year = Label(gui, text = "Enter Year", bg = "light gray",
              font = ("calibri", 18, 'bold','italic'))
	
	
	year_field = Entry(gui)

	Show = Button(gui, text = "Show Calendar",
               font = ("calibri", 18, 'bold','italic'),
						bg = "light gray", command = showCal)
	
	Exit = Button(gui, text = "Exit",
               font = ("calibri", 18,'italic'),bg = "light gray",command = exit)
    
    
cal.grid(row = 0, column = 1)  
 
year.grid(row = 1, column = 1)
 
year_field.grid(row = 2, column = 1)
 
Show.grid(row = 3, column = 1)
 
Exit.grid(row = 4, column = 1)

gui.mainloop()
    