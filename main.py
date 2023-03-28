import datetime
from tkinter import *
from geo import Response
from weather import Response_Weather
from beautiful import InterActiveButton
import webbrowser as wb
# mar 28
# mar 28
# ammar abu fadhel
FIX_COLOUR = "#77e8fb"
BG_WIND = "#083657"
Font_add = ("arial", 12, "bold")
window = Tk()
window.config(pady=20, padx=20)
window.config(bg=FIX_COLOUR)
window.title("Weather")
file = PhotoImage("images/sunny_sun_cloud_weather_cloudy_icon_194237.ico")
window.iconbitmap(file)
title_label = Label(text="API Cuaca", font=('arial', 32, 'bold'), bg=FIX_COLOUR)
title_label.grid(columnspan=2, column=0, row=0)
image_coulds = PhotoImage(file="images/cool bet.png")
image_rain = PhotoImage(file="images/tes4.png")
image_canvas_clouds = PhotoImage(file="images/5950875.png")
image_rain_temp = PhotoImage(file="images/low-temperature (1).png")
image = PhotoImage(file="images/fix_normal.png")
images_clouds = PhotoImage(file="images/tes.png")
image_add_temp = PhotoImage(file="images/hot (1).png")
button_animated = PhotoImage(file="images/play (1).png")

i = 0
j = 0
k = 0

colour_list = [FIX_COLOUR, BG_WIND]
colour_title_label = ["#161616", "#DDDDDD"]
colour_button = ["#083657"]


def enter_click():
    global i
    global j
    global k
    try:
        data_entry = entry_user.get()
        data = Response(data_entry)

        def open_web():
            return wb.open(data.content_map())

        data_weather = Response_Weather(data.latitude_())
        label_temp = round(data_weather.temp_main(), 1)
        button_link = InterActiveButton(window, text="Maps", width=200, height=25, command=open_web)
        button_link.config(bg=colour_button[0], border=2)
        button_link = canvas.create_window(225, 450, window=button_link)
        if i == 0:
            canvas.itemconfig(item_main, text=f"{label_temp}°C")
            canvas.itemconfig(item_weather, text=f"{data_weather.weather()}")
            canvas.itemconfig(item_over, text=f"({data_weather.temp_description()})")
        elif i == 1:
            canvas.itemconfig(item_main, text=f"{label_temp}°C")
            canvas.itemconfig(item_weather, text=f"{data_weather.weather()}")
            canvas.itemconfig(item_over, text=f"({data_weather.temp_description()})")
        i = 1
        if data_weather.weather() == "Clouds":
            # canvas
            canvas.itemconfig(canvas_image, image=image_canvas_clouds)
            # temperature image
            canvas.itemconfig(canvas_add_temp, image=image_coulds)
            j = 1
            k = 1
        elif data_weather.weather() == "Rain":
            canvas.itemconfig(canvas_add_temp, image=image_rain_temp)
            canvas.itemconfig(canvas_image, image=image_rain)
            j = 1
        else:
            j = 0

        # time
        canvas.itemconfig(time_, text=f"Time : {datetime.datetime.now().hour}:{datetime.datetime.now().minute}"
                          ,fill=colour_title_label[k])
        canvas.itemconfig(time_zone,text=f"Time Zone : {data.time_zone()}",fill=colour_title_label[k])
        # line
        canvas.create_line(125, 230, 345, 230, fill="#242424", width=5)
        # formatted
        canvas.itemconfig(text_formatted, text=f"{data.content_formated()}\n"
                                               f"{data.latitude_()}", fill=colour_title_label[j])
        # feels like
        canvas.itemconfig(feels_like, text=f"feels like : {data_weather.feels_like()}", fill=colour_title_label[k])
        # pressure
        canvas.itemconfig(pressure, text=f"Pressure : {data_weather.presure()}", fill=colour_title_label[k])
        # wind
        canvas.itemconfig(wind, text=f"Wind : {data_weather.wind()}", fill=colour_title_label[k])
        # clouds
        canvas.itemconfig(clouds, text=f"Clouds : {data_weather.clouds()}", fill=colour_title_label[k])

        # coord
        button_entry.config(bg=colour_list[j], activebackground=colour_list[j])
        window.config(bg=colour_list[j])
        point_entry.config(bg=colour_list[j])

        title_label.config(fg=colour_title_label[j])
        title_label.config(bg=colour_list[j])
        canvas.config(highlightthickness=0, bg=colour_list[j])
        # label point
        point_entry.config(fg=colour_title_label[j])
        print(data_weather.main(), '\n')
        print(data_weather.temp(), '\n')
    except IndexError:
        pass


entry_user = Entry(width=30, font=('arial', 12, 'bold'))
entry_user.grid(row=1, column=0, ipadx=10, ipady=5)
button_entry = Button(window, text="Find", font=('arial', 13, 'bold'), bg=colour_list[i],
                      command=enter_click, image=button_animated, activebackground=colour_list[i], borderwidth=0
                      , height=70, cursor="hand2", )
button_entry.grid(row=1, column=1)
entry_user.focus()

point_entry = Label(text="Format : city,country", font=('arial', 10, 'italic')
                    , bg=FIX_COLOUR)
point_entry.grid(row=2, column=0)

canvas = Canvas(width=470, height=470, bg=FIX_COLOUR, highlightthickness=0)
canvas.grid(row=3, column=0, columnspan=2)
canvas_image = canvas.create_image(235, 240, image=image)
canvas_add_temp = canvas.create_image(404, 80, image=image_add_temp)

item_main = canvas.create_text(250, 180, text="", font=("arial", 70, 'bold'))
item_weather = canvas.create_text(225, 250, text="", font=('arial', 15, 'bold'))
item_over = canvas.create_text(225, 268, text="", font=('arial', 12, 'italic'))

text_formatted = canvas.create_text(100, 20, text="", font=("arial", 10, 'italic'), activefill="red")
feels_like = canvas.create_text(100, 305, text="", font=Font_add, activefill="red", )
pressure = canvas.create_text(350, 305, text="", font=Font_add, activefill="red")
wind = canvas.create_text(100, 335, text="", font=Font_add, activefill="red")
clouds = canvas.create_text(350, 335, text="", font=Font_add, activefill="red")
time_ = canvas.create_text(350, 365, text="", font=Font_add, activefill="red")
time_zone = canvas.create_text(100, 365, text="", font=Font_add, activefill="red")

window.mainloop()
