from pathlib import Path
import shutil
from files.credentials import cred
import time as t
import pyautogui as pa


class In:
    def run(self):
        if cred.login == 'xcelis@xcelis.com.br':
            self.check_file()
            self.start()   
            self.entrar()    
            self.cred()
            self.cancel()
            self.rel_linhas()
        else:
            self.check_file()
            self.start()   
            self.entrar()
            self.cred2()
            self.rel_linhas()
        

    def check_image(self,img,cfdc):
        status = None
        while status == None:
            status = pa.locateCenterOnScreen(img,confidence=cfdc)
            t.sleep(.5)
        return status


    def check_file(self):
        caminho = Path.cwd()/'databases'
        if caminho.exists() == False:
            Path(Path.cwd()/'databases').mkdir()
        if(caminho/Path("inbound.xlsx")).exists():
            (caminho/Path("inbound.xlsx")).unlink()
        if(caminho/Path("outbound.xlsx")).exists():
            (caminho/Path("outbound.xlsx")).unlink()
        if(caminho/Path("pendencia.xlsx")).exists():
            (caminho/Path("pendencia.xlsx")).unlink()

    def start(self):
        pa.hotkey("winleft","r")
        self.check_image("images/executar.png",0.6)
        pa.write("chrome")
        t.sleep(1)
        pa.press("enter")
        t.sleep(3)
        pa.hotkey("ctrl","shift","n")
        t.sleep(1)
        pa.hotkey("alt","tab")
        t.sleep(1)
        pa.hotkey("ctrl","w")
        self.check_image("images/anonima.png",0.6)
        link = r'https://camop-sci.sce.manh.com/bi/'
        pa.write(f'{link}')
        t.sleep(1)
        pa.press("enter")
    
    def entrar(self):
        t.sleep(2)
        x,y =self.check_image("images/sci.png",0.6)
        pa.click(x,y)
        pa.press("up",2,0.4)
        t.sleep(0.5)
        pa.press("enter")

    def cred(self):
        pa.moveTo(20,20)
        x,y =self.check_image("images/cred.png",0.6)
        pa.write(f"{cred.login}")
        t.sleep(0.5)
        pa.press("enter")
        x,y =self.check_image("images/pass.png",0.6)
        pa.click(x,y)
        t.sleep(1)
        pa.write(f"{cred.senha}")
        t.sleep(0.5)
        pa.press("enter")

    def cred2(self):
        pa.moveTo(20,20)
        x,y =self.check_image("images/cred.png",0.6)
        pa.write(f"{cred.login}")
        t.sleep(0.5)
        pa.press("enter")
        x,y =self.check_image("images/ad1.png",0.8)
        pa.write(f"{cred.login}")
        t.sleep(0.5)
        pa.press("enter")
        x,y =self.check_image("images/ad2.png",0.8)
        pa.write(f"{cred.senha}")
        t.sleep(0.5)
        pa.press("enter")
        x,y =self.check_image("images/ad3.png",0.8)
        t.sleep(0.5)
        pa.press("enter")
        
    def cancel(self):
        pa.moveTo(20,20)
        x,y =self.check_image("images/cancel.png",0.7)
        pa.click(x,y)

    def rel_linhas(self):
        x,y =self.check_image("images/pasta1.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/pasta2.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/pasta3.png",0.8)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/linhas.png",0.8)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/mapaIn.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/salvar.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        arquivo_movido = False
        for i in range(20):
            if arquivo_movido:
                break

            caminho_origem = Path.home()/'Downloads'
            caminho_destino = Path.cwd()/'databases'
            for arquivo in caminho_origem.iterdir():
                while arquivo.is_file() and arquivo.name.endswith("load"):
                    t.sleep(1)
                if (caminho_origem/Path("mapa linhas in.xlsx")).exists():
                    shutil.move((caminho_origem/Path("mapa linhas in.xlsx")),(caminho_destino/Path("inbound.xlsx")))
                    arquivo_movido = True
                    break
            t.sleep(5)
        x,y =self.check_image("images/pasta1.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/mapaOut.png",0.9)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/salvar.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        arquivo_movido = False
        for i in range(20):
            if arquivo_movido:
                break
            caminho_origem = Path.home()/'Downloads'
            caminho_destino = Path.cwd()/'databases'
            downloads_new = len(list((Path.home()/'Downloads').iterdir()))
            for arquivo in caminho_origem.iterdir():
                while arquivo.is_file() and arquivo.name.endswith("load"):
                    t.sleep(1)
                if (caminho_origem/Path("mapa linhas out.xlsx")).exists():
                    shutil.move((caminho_origem/Path("mapa linhas out.xlsx")),(caminho_destino/Path("outbound.xlsx")))
                    arquivo_movido = True
                    break
            t.sleep(5)
        x,y =self.check_image("images/pasta1.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/basePO.png",0.7)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/dataIni.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        t.sleep(0.7)
        pa.press("tab")
        t.sleep(0.7)
        pa.write(f"{cred.data}")
        x,y =self.check_image("images/concluir.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        x,y =self.check_image("images/salvar.png",0.6)
        pa.click(x,y)
        pa.moveTo(20,20)
        arquivo_movido = False
        for i in range(20):
            if arquivo_movido:
                break
            caminho_origem = Path.home()/'Downloads'
            caminho_destino = Path.cwd()/'databases'
            for arquivo in caminho_origem.iterdir():
                while arquivo.is_file() and arquivo.name.endswith("load"):
                    t.sleep(1)
                if (caminho_origem/Path("Base Pendência PO_ASN.xlsx")).exists():
                    shutil.move((caminho_origem/Path("Base Pendência PO_ASN.xlsx")),(caminho_destino/Path("pendencia.xlsx")))
                    arquivo_movido = True
                    break
            t.sleep(5)
        pa.hotkey("ctrl","w")