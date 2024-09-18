#abrir o google
#entrar no site
#fazer login

import time
import pyautogui


pyautogui.PAUSE = 3




pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.PAUSE = 3

pyautogui.click(x=396, y=331)
pyautogui.click(x=628, y=42)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=507,y=373)
pyautogui.write("barbara.login")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("enter")


#first step ok

import pandas as pd

data = pd.read_csv("paradise.csv")
print(data)



for line in data.index:
     pyautogui.click(x=445, y=255)
     codigo =data.loc[line, "codigo"]
     pyautogui.write(str(codigo))
     pyautogui.press("tab")
     pyautogui.write(str(data.loc[line, "marca"]))
     pyautogui.press("tab")
     pyautogui.write(str(data.loc[line, "tipo"]))
     pyautogui.press("tab")
     pyautogui.write(str(data.loc[line, "categoria"]))
     pyautogui.press("tab")
     pyautogui.write(str(data.loc[line, "preco_unitario"]))
     pyautogui.press("tab")
     pyautogui.write(str(data.loc[line, "custo"]))
     pyautogui.press("enter")
     time.sleep(2)
     pyautogui.scroll(5000)












