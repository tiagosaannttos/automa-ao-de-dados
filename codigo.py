#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui.hotkey
#pyautogui.scroll

import pyautogui
import time

pyautogui.PAUSE =0.5


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=636, y=373)
pyautogui.hotkey("ctrl","a")
pyautogui.write("tiiagosaantos@gmail.com")

pyautogui.press("tab")
pyautogui.write("minhasenha")

pyautogui.click(x=657, y=525)

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)



for linha in tabela.index:
    pyautogui.click(x=573, y=256)
    
    codigo=str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    
    
    marca=str(tabela.loc[linha,"marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)
    
    tipo=str(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
    
    categoria=str(tabela.loc[linha,"categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)
    
    preco=str(tabela.loc[linha,"preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)
    
    custo=str(tabela.loc[linha,"custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    
    pyautogui.press("tab")
    obs=str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)
    
               