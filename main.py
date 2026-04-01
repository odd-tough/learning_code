import tkinter
import requests
from dotenv import load_dotenv
import os
image=None


name1="default"
name2="default"

load_dotenv()
api_key = os.getenv("API_KEY")


# from PIL import Image
#
# img = Image.open("hello1.png")
# cropped = img.crop(img.getbbox())
#
# cropped.save("love.png")


def love_chinnam(love_percentage,response_love):
    global image
    image = tkinter.PhotoImage(file="love.png")
    canvas = tkinter.Canvas(width=300, height=295, bg="white", highlightthickness=0)
    canvas.create_image(150, 207, image=image)
    canvas.create_text(150, 220, text=love_percentage, font=("arial", 25, "bold"))
    canvas.grid(row=3, column=0, columnspan=2)

    label_response = tkinter.Label(text=response_love,wraplength=150,bg="white",font=("arial",10,"italic"))
    label_response.grid(row=4, column=0, columnspan=2)

def names():
    global image
    name1=entry_name1.get()
    name2=entry_name2.get()
    parameters={"name1":name1,
                "name2":name2}
    headers = {
        "X-API-Key":api_key,
    }
    response=requests.get(url="https://api.apiverve.com/v1/lovecalculator",params=parameters,headers=headers)
    data=response.json()
    love_percentage=data["data"]["lovePercentage"]
    response_love=data["data"]["response"]
    love_chinnam(love_percentage,response_love)

window=tkinter.Tk()
window.title("love calculator")
window.config(padx=50,pady=50,bg="white")
love_chinnam("","")
label_name1=tkinter.Label(text="your name",font=("Arial",10,"bold"),bg="white")
label_name1.grid(row=0,column=0)
entry_name1=tkinter.Entry(width=30,font=("Arial",10,"normal"))
entry_name1.grid(row=0,column=1)

label_name2=tkinter.Label(text="crush's name",font=("Arial",10,"bold"),bg="white")
label_name2.grid(row=1,column=0)
entry_name2=tkinter.Entry(width=30,font=("arial",10,"normal"))
entry_name2.grid(row=1,column=1)

button_name1=tkinter.Button(text="Enter",command=names,width=30,bg="red",fg="white")
button_name1.grid(row=2,column=1)

window.mainloop()