import tkinter

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top = tkinter.Frame(self.main_window)
        self.mid = tkinter.Frame(self.main_window)
        self.bot = tkinter.Frame(self.main_window)
        

        self.prompt = tkinter.Label(self.top, text="Enter the hash")
        self.hash_entry = tkinter.Entry(self.top,width=32)

        self.prompt.pack(side='left')
        self.hash_entry.pack(side='left')

        self.out = tkinter.Label(self.mid, text='Password: ')
        self.value = tkinter.StringVar()

        self.pwd_out = tkinter.Label(self.mid,textvariable=self.value)
        
        self.out.pack(side='left')
        self.pwd_out.pack(side='left')

        self.go = tkinter.Button(self.bot, text="Enter",command=self.handler)
        self.quit = tkinter.Button(self.bot,command=self.main_window.destroy)

        self.go.pack(side='left')
        self.quit.pack(side='left')

        self.top.pack()
        self.mid.pack()
        self.bot.pack()

        tkinter.mainloop()

    def handler(self):
        inp = self.hash_entry.get()
        if (inp=="41933e60e9c19b866b3d68864727afe7"):
            o = "123456"
            self.value.set(o)        
        elif(inp=="25f9e794323b453885f5181f1b624d0b"):
            o = "123456789"
            self.value.set(o) 
        elif(inp=="827ccb0eea8a706c4c34a16891f84e7b"):
            o = "12345"
            self.value.set(o)   
        elif(inp=="d8578edf8458ce06fbc5bb76a58c5ca4"):
            o = "qwerty"
            self.value.set(o) 
        elif(inp=="5f4dcc3b5aa765d61d8327deb882cf99"):
            o = "password"
            self.value.set(o)         
        elif(inp=="6e5f603247a61d89625127f3f67836a7"):
            o = "12345678"
            self.value.set(o)         
        elif(inp=="c809ba39aef32fb858f1fee4cb392588"):
            o = "111111"
            self.value.set(o) 
        elif(inp=="4297f44b13955235245b2497399d7a93"):
            o = "Password: 123123"
            self.value.set(o)
        else:
            o = "NOT A COMMON PASSWORD"
            self.value.set(o)
            
if __name__=='__main__':
    g = GUI()