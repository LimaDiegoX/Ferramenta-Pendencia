from tkinter import *
import time as t
import pyautogui as pa
from files.incc_in import In
import xlwings as xw
from pathlib import Path

class Param:    
    lista = []       

    def executar(self):

        with open(r"files\intervalo.txt","r") as file:
            segundos = int(file.read()) * 1000

        named_tuple = t.localtime() # get struct_time
        time_string = t.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        self.lista.append(time_string)
        self.text_update.insert(END,self.lista[-1])
        In().run()
        wb = xw.Book(f"{Path.cwd()}/Visão INCC_Final.xlsm")
        send_email = wb.macro("RunAll.Run")
        send_email()
        wb.save()
        # wb.app.quit()
        # t.sleep(10)
        # wb = xw.Book(f"{Path.cwd()}/Visão INCC_Final.xlsm")
        self.window.after(segundos,self.executar)
        
    # def change_window(self):
    #     print("Estou no changewindow")
    #     wb = xw.Book(f"{Path.cwd()}/INCC.xlsm")

    #     sheet_name = 'Dash'
    #     sheet = wb.sheets[sheet_name]
    #     sheet.activate()
    #     t.sleep(2)
    #     sheet_name = 'Base PO'
    #     sheet = wb.sheets[sheet_name]
    #     sheet.activate()
    #     self.window.after(2000,self.executar)
        
    def __init__(self,texto:str):
        width, height = pa.size()
        self.window = Tk()
        wind_width,wind_height = 445,341
        windx,windy = int((width/2)-(wind_width/2)),int((height/2)-(wind_height/1.5))
        self.window.geometry(f"{wind_width}x{wind_height}+{windx}+{windy}")
        self.window.configure(bg = "#ffffff")
        canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 341,
            width = 445,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        text_hora = Label(
            bd=0,
            font="Judson 12 bold",
            foreground="#D6E2F6",
            bg="#192B4B",
            anchor="w",
            text=texto
        )

        text_hora.place(
            x=26,
            y=190,
            width=140,
            height=40
        )

        self.text_update = Listbox(
            bd=0,
            font="Judson 12 bold",
            foreground="#D6E2F6",
            bg="#192B4B",
            # bg="#D6E2F6",
            # anchor="nw",
            # c
        )

        self.text_update.place(
            x=240,
            y=100,
            width=175,
            height=200
        )

        self.window.iconbitmap(r"icones\in_out_down.ico")

        self.window.title("Inb/Out Downloader")


        background_img = PhotoImage(file = r"files\parameters\background.png")
        background = canvas.create_image(
            222.5, 167.0,
            image=background_img)
        
        self.executar()

        self.window.resizable(False, False)
        self.window.mainloop()
