from customtkinter import *
from Threads.Process import Process



class UI:

    def screen(self):
        def handleClick():
            # print("Clicked")
            if not path.get():
                return -1
            print("Clicked", path.get())
            try:
                progressbar.start()
                path.configure(state="disabled")
                Process(path.get()).start()
                app.destroy()
            except Exception as e:
                print('Error', e)
                progressbar.set(1)
                progressbar.stop()
        app = CTk()
        set_default_color_theme("green")
        app.geometry("600x500")
        app.title("Notes Organizer")
        path = CTkEntry(master = app, placeholder_text="enter path ...", width=300,height=40, text_color="#FFCC70")
        run = CTkButton(master=app, width=100,height=40, text="Organize", command=handleClick)
        progressbar = CTkProgressBar(app, orientation="horizontal",determinate_speed = 0.3)
        progressbar.set(0)
        path.place(relx=0.5, rely = 0.4, anchor = "center")
        run.place(relx=0.5, rely = 0.5, anchor = "center")
        progressbar.place(relx=0.5, rely = 0.65, anchor = "center")
        app.mainloop()