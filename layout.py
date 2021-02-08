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

# SINGLETON DESIGN PATTERN

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
        self.TITLE(self.__title)

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

    def wrap_up(self):
        self.mainloop()
#

Root = Layout()
Root.wrap_up()




''''


        # Declarar protocolos (links entre ventana events y script) parte de Tk()
        
       



        # Protocolos de ventana
       

        # Crear Frame dentro de Tk
        HomePage(self, "assets\\home-bkg.png")
        
    def set_root_icon()
 
            
'''