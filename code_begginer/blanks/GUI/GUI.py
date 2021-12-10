from tkinter import *

import webbrowser

if __name__ == "__main__":
    import webbrowser
button_clicked_count = 0

def click():
    global button_clicked_count
    button_clicked_count+=1
    print(button_clicked_count)
    webbrowser.open_new(r"https://market.yandex.ru/")


shwindow = Tk() # instatiate an instance of a window 
shwindow.geometry("300x300")
shwindow.title("GUI first")

icon = PhotoImage(file="python.png")
shwindow.iconphoto(True, icon)
shwindow.config(background="#fff", padx=500)

photo = PhotoImage(file="photo.png")

label = Label(shwindow, text="Проверка цен на Яндекс Маркет", 
                        font=("Open Sans", 30, "bold"), 
                        fg="#282A36", bg="#fff", bd=0,
                        relief=RAISED,
                        compound="bottom",
                        padx=20, pady=20,
                        image=photo,
                        )

# entry = Entry(shwindow,
#               font=("Open Sans", 25))
# entry.pack(side=LEFT)

button = Button(shwindow, 
                text="Парсить Yandex Market",
                command=click,
                font=("Open Sans", 18, "bold"),
                fg="#282A36", bd=0, bg="#fafafa",
                activeforeground="#282A36",
                activebackground="#fafafa",
                compound="bottom")

shwindow.mainloop() 
# place window in computer screen/

button.pack()        
# shwindow это название окна. 
# Впервую очередь мы образаемся к нему, 
# а потом пишем все параметры

label.pack()
# label.place() позволяет задать координаты x, y =