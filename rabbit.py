import tkinter as tk
import tkinter.font as tkFont
import tkinter.scrolledtext as ts 
from tkinter import messagebox
import os
import time as t
import subprocess as sb
import simpleaudio as sa
from PIL import Image, ImageTk # NON-STANDARD Allows the use of different image formats
import vlc # NON-STANDARD

# Layout (tk.Tk) -> Rabbit (tk.Canvas)

class Layout(tk.Tk):
    def __init__(self):

        super().__init__()

        self.__title = "rabbit app"
        self.__icon = "assets//rabbit-icon.ico"
        self.__width = int(self.winfo_screenwidth())
        self.__height = int(self.winfo_screenheight())
        self.__close_message = "Kill rabbit?"
        
        self.geometry(f"{self.__width}x{self.__height}")
        self.title(self.__title)
        self.attributes("-topmost", True) # Put the layout at the top of any window
        self.iconbitmap(self.__icon)

        # Layout protocols
        self.protocol("WM_DELETE_WINDOW", self.close_layout)

    def set_title(self, title):
        self.__title = title
        self.title(self.__title)

    def get_title(self):
        return self.__title

    def set_icon(self, icon):
        self.__icon = icon

    def get_icon(self):
        return self.__icon

    def set_dimensions(self, width, height):
        self.__width = width
        self.__height = height
        self.geometry(f"{self.__width}x{self.__height}")

    def get_dimensions(self):
        return self.__width, self.__height

    def close_layout(self):
        if messagebox.askokcancel(message=self.__close_message, title=self.__title):
            self.destroy()

    def put_it_all_together(self):
        self.mainloop()




class Rabbit(tk.Canvas):
    def __init__(self, meadow):

        self.__meadow = meadow
        self.__bkg = "assets//meadow-bkg.png"
        self.__width = 1920
        self.__height = 1080
        self.__border_width = 1

        super().__init__(self.__meadow, width = self.__width, height = self.__height)

        self.__smallFont = tkFont.Font(family="Open Sans", size=8)
        self.__mediumFont = tkFont.Font(family="Open Sans", size=12)
        self.__bigFont = tkFont.Font(family="Open Sans Semibold", size=25)

        self.bkg = Image.open(self.__bkg)
        self.bkg = self.bkg.resize((self.__width, self.__height))
        self.img = ImageTk.PhotoImage(self.bkg)
        self.create_image(0, 0, anchor = tk.NW, image=self.img)

    def set_bkg(self, bkg):
        self.__bkg = bkg
    
    def get_bkg(self):
        return self.__bkg

    def set_border_width(self, border_width):
        self.__border_width = border_width
    
    def get_border_width(self):
        return self.__border_width


    def spawn_rabbit(self):
        self.place(x = 0, y = 0)

Root = Layout()

StartPage = Rabbit(Root)
StartPage.spawn_rabbit()

Root.put_it_all_together()


'''


         # Entrar Button
        self.addWidget(tk.Button(self, 
                                    text="Entrar", 
                                    anchor = tk.CENTER,
                                    bg = "#FE8C33",
                                    foreground = "#B4301A",
                                    width = "99",
                                    height = "0",
                                    bd = "3",
                                    font = self.fontStyle,
                                    command = self.go_next_page), 979, 1000)

        # Author text  
        self.create_text(1759,900, fill="black",
                                        text="Desarrollado por Jorge Flores",
                                        justify = tk.RIGHT,
                                        font = self.fontStyle2)


        # CANVAS Geometry Manager
        
    
    def addWidget(self, widget, x, y):
        self.create_window(x, y, anchor=tk.CENTER, window=widget)
        return widget
    
    def go_next_page(self):
        
        SuertePage(self.ROOT, "assets\\suerte-bkg.png")
        self.destroy()

'''