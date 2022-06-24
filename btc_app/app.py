import tkinter as tk
import requests
import webbrowser
from tkinter import messagebox
import random
import datetime
import itertools
def message():
    qiwi_api=messagebox.askyesno(message=f"The amount you will pay - {get_entered_amount()}.\nDo you want to proceed?" ,title="Continuation")
    if qiwi_api==True:
        qiwi_api_function()
    elif qiwi_api==False:
        quit

def get_entered_amount():
    entered_amount=int(entry.get())
    #price=main()
    #amount_in_btc="{:.8f}".format(entered_amount/price)
    return "{:.2f}".format(entered_amount)

def qiwi_api_function():
    billid=""
    for i in range(1,15):
        rand=random.randrange(1,1000)
        billid+=str(rand)
    hour=1
    date=datetime.datetime.now()
    added=datetime.timedelta(hours=hour)
    expirationdate=date+added
    expirationdate=expirationdate.strftime("%Y-%m-%dT%H:%M:%S+03:00")
    secret_key="eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InF1OXA1NC0wMCIsInVzZXJfaWQiOiI3OTAzNzk1NDU0MyIsInNlY3JldCI6IjZhMTM3ZGI4M2NkYjU3OTUxOWFhMzM2Yzk3ODRiNGJmYjYwMTg0OGNlYjBiZWI3YzE2YmEzMzQ5ZTI5YjVjYjIifX0="
    url=f"https://api.qiwi.com/partner/bill/v1/bills/{billid}"
    headers={"Authorization":f"Bearer {secret_key}",
    "Content-Type": "application/json",
    "Accept": "application/json"}
    parameters={"amount":
    {"value":f"{get_entered_amount()}",
    "currency":"RUB"},
    "expirationDateTime":f"{expirationdate}"}
    r=requests.put(url=url,json=parameters,headers=headers).json()
    webbrowser.open_new(url=r["payUrl"])
    while True:
        r=requests.get(url=url,headers=dict(itertools.islice(headers.items(),2))).json()
        if r["status"]["value"]=="PAID":
            messagebox.showinfo(title="",message="Transaction succeeded")
            break


    
    


main1=tk.Tk()
main1.geometry("500x700")
main1.title("BTC APP")
frame=tk.Frame(main1,bg="#FFDE03",borderwidth=2,relief="raised")
frame.place(height=100,width=500,x=0,y=250)
entry=tk.Entry(frame,bg="#D8DEE9",relief="flat",font="Helvetica 20 bold")
entry.place(height=40,width=200,x=100,y=30)
button=tk.Button(frame,text="Calculate",command=message)
button.place(height=40,x=325,y=30)
text=tk.Label(frame,font=("Helvetica 10 bold"),text="How much do you want to pay?(RUB)")
text.place(x=75,y=10)
main1.mainloop()
