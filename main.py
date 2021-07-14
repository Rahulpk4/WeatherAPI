import requests
import tkinter
from tkinter import *
import customtkinter as ct
from PIL import ImageTk, Image

class WeatherApp:
    def __init__(self, win):
        self.win = win
        self.win.geometry("500x500")
        self.win.title('Weather App')
        self.win.iconbitmap("Images/weather.ico")
        self.win.resizable(False,False)

        self.frame1 = Frame(self.win, bg='#323736')
        self.frame1.place(x=0,y=0, width=500, height=500)
        self.img = Image.open('Images/logo.png')
        self.gameImage = ImageTk.PhotoImage(self.img)
        self.logo = Label(self.frame1, image=self.gameImage, bg="#323736")
        self.logo.pack(fill=X, padx=20,pady=20)


        self.search_frame = ct.CTkFrame(master=self.frame1, fg_color="#7A7477", width=350, height=50, corner_radius=10)
        self.search_frame.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)
        self.entry = ct.CTkEntry(master=self.search_frame,width=150,height=25,corner_radius=10,text_color=("#655A5F","#4D484A"))
        self.entry.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)
        self.button = ct.CTkButton(master=self.search_frame, text="Check", text_font=("Calibri",12,'bold'), text_color='white', fg_color="#353334", corner_radius=10, command=lambda:self.weatherfetch(self.entry.get()))
        self.button.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

        self.mainframe = ct.CTkFrame(master=self.frame1,width=350,height=250,corner_radius=10)
        self.mainframe.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

    def weatherfetch(self, name):
        city = name
        api = 'url' + str(city) + '+Access_token'
        json_data = requests.get(api).json()
        self.coord = ct.CTkLabel(master=self.mainframe,width=200,height=30,text=f"Lat:{json_data['coord']['lat']} & Long:{json_data['coord']['lon']}",text_color="#464642",text_font='Calibri',corner_radius=8)
        self.coord.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.cityname = ct.CTkLabel(master=self.mainframe,width=400,height=30,text=f"{json_data['name']} ({json_data['sys']['country']})",text_color="#464642",text_font='Calibri',corner_radius=8)
        self.cityname.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.weathertype = ct.CTkLabel(master=self.mainframe,width=400,height=30,text=f"Weather: {json_data['weather'][0]['main']}",text_color="#464642",text_font='Calibri',corner_radius=8)
        self.weathertype.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.temp = ct.CTkLabel(master=self.mainframe,width=400,height=30,text=f"Temperature: {round(json_data['main']['temp'] - 273.15, 2)}, Feels Like: {round(json_data['main']['feels_like'] - 273.15, 2)}",text_color="#464642",text_font=('Calibri', 10),corner_radius=8)
        self.temp.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.minmax = ct.CTkLabel(master=self.mainframe,width=400,height=30,text=f"Minimum Temperature: {round(json_data['main']['temp_min'] - 273.15, 2)}, Maximum Temperature: {round(json_data['main']['temp_max'] - 273.15,2)}",text_color="#464642",text_font=('Calibri',10),corner_radius=8)
        self.minmax.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

if __name__ == "__main__":
    win = Tk()
    obj = WeatherApp(win)
    win.mainloop()