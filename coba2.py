import pyautogui as pg
import webbrowser as web
import time
import os
import pandas as pd
trainFile = os.path.join('D:',os.sep,'project','jualan','lead.csv')
data = pd.read_csv(trainFile)
#data = pd.read_csv("lead.csv")
data_dict = data.to_dict('list')
leads = data_dict['LeadNumber']
messages = data_dict['Message']
combo = zip(leads,messages)
file = "E:\coba22.png"
first = True
for lead,message in combo:
    time.sleep(8)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    time.sleep(8)
    pg.click(x=481, y=692)
    pg.click(x=481, y=630)
    pg.moveTo(553, 767, 1)
    pg.typewrite(file,0.1)                   
    #pg.click(x=522, y=442)
    pg.press('enter')    
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')