import xlwings as xw

# Specifying a sheet
ws = xw.Book("Visão INCC_Final.xlsm").sheets['Parâmetros']
USER = ws.range("C12:C13").value
DATA = ws.range("L3").value
DATA = DATA.strftime("%d/%m/%Y") 
# v2 = ws.range("F5").value

class cred:
    login = USER[0]
    senha = USER[1]
    data = DATA