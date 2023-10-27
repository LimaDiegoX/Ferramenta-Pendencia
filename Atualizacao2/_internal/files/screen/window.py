from tkinter import *
from tkinter import messagebox
from files.parameters.param import Param
import pyautogui as pa


class Window:
    def atualizar_texto(self,event=None):
        texto1 = self.entry0.get()
        texto2 = self.entry1.get()
        try:
            seconds = (int(texto1)*3600)+(int(texto2)*60)
            texto = f"A cada: {texto1}h{texto2}min"
            self.text_hora.config(text=texto)
        except:
            if texto1 == "":
                texto1 == "00"
            if texto2 == "":
                texto2 == "00"
            texto = f"A cada: {texto1}h{texto2}min"
            self.text_hora.config(text=texto)
        return seconds,texto
        
    def salvar_intervalo(self):
        sec,info = self.atualizar_texto()
        if sec>0:
            with open("files/intervalo.txt","w") as file:
                valor = str(sec)
                file.write(valor)
            
            self.window.destroy()
            tela_nova = Param(info)
            
        else:
            messagebox.showinfo("Atenção!!!","Intervalo incorreto")
        
    def validar_entrada(self,P):
        if P.isdigit() and len(P)<=2:       
            return True
        elif P == "":
            return True
        else:
            return False
        
    def __init__(self):
        width, height = pa.size()
        
        self.window = Tk()
        wind_width,wind_height = 445,341
        windx,windy = int((width/2)-(wind_width/2)),int((height/2)-(wind_height/1.5))
        self.window.geometry(f"{wind_width}x{wind_height}+{windx}+{windy}")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 341,
            width = 445,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.window.iconbitmap(r"icones\in_out_down.ico")

        self.window.title("Inb/Out Downloader")

        self.background_img = PhotoImage(file = r"files\screen\background.png")
        self.background = self.canvas.create_image(
            222.5, 170.5,
            image=self.background_img)

        self.img0 = PhotoImage(file = r"files\screen\img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.salvar_intervalo,
            relief = "flat")

        self.b0.place(
            x = 120, y = 283,
            width = 206,
            height = 34)

        self.entry0_img = PhotoImage(file = r"files\screen\img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(
            70.0, 163.5,
            image = self.entry0_img)

        self.entry0 = Entry(
            validate="key",
            validatecommand=(self.window.register(self.validar_entrada), "%P"),
            bd = 0,
            justify="center",
            bg = "#ccd3df",
            highlightthickness = 0)

        self.entry0.place(
            x = 41.0, y = 138,
            width = 58.0,
            height = 49)

        self.entry0.insert(0,"00")

        self.entry1_img = PhotoImage(file = "files\screen\img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(
            70.0, 228.5,
            image = self.entry1_img)

        self.entry1 = Entry(
            validate="key",
            validatecommand=(self.window.register(self.validar_entrada), "%P"),
            bd = 0,
            justify="center",
            bg = "#ccd3df",
            highlightthickness = 0)

        self.entry1.place(
            x = 41.0, y = 203,
            width = 58.0,
            height = 49)

        self.entry1.insert(0,"00")

        self.entry0.bind("<KeyRelease>",self.atualizar_texto)
        self.entry1.bind("<KeyRelease>",self.atualizar_texto)

        self.text_hora = Label(
                bd=0,
                font="Helvetica 8 bold",
                foreground="#0B1629",
                bg="#ccd3df",
                text="Intervalo: "
            )

        self.text_hora.place(
            x=266,
            y=220,
            width=100,
            height=25
        )

        
        self.window.resizable(False, False)
        self.window.mainloop()