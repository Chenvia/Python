from Tkinter import *
    

class gui():

    def __init__(self,window):

        from retGCstoredpasswd import retgcstoredpasswds, AccessError
        from sys import exit
        import platform
        import tkMessageBox

        self.exit = exit
        self.window = window
        self.window.title("GCredDump")

        bufferhead = Label(window)
        self.urlhead = Label(window, text="URL:",justify="center")
        self.unamehead = Label(window, text="User Name:",justify="center")
        self.passwd = Label(window, text="Password:",justify="center")
        bufferhead.grid(row=0,columnspan=2)
        self.urlhead.grid(row=1,column=0)
        self.unamehead.grid(row=1,column=1)
        self.passwd.grid(row=1,column=2)

        try:
            results = retgcstoredpasswds(platform.version())
        except AccessError as e:
            text = str(e)
            if tkMessageBox.showerror("Fatal Error!",text) == 'ok':
                root.destroy()
                self.exit()
                
        except ValueError as e:
            text = str(e)
            if tkMessageBox.showerror("Fatal Error!",text) == 'ok':
                root.destroy()
                self.exit()

        if not results:
            c1 = Entry(window, justify="center")
            c2 = Entry(window, justify="center")
            c3 = Entry(window, justify="center")
            c1.grid(row=2,column=0)
            c2.grid(row=2,column=1)
            c3.grid(row=2,column=2)
            c1.insert(0, 'N/A')
            c2.insert(0,"No Data Found!")
            c3.insert(0, 'N/A')
            c1.config(state='readonly')
            c2.config(state='readonly')
            c3.config(state='readonly')

        else:
            print results
            for x in results:
                c1 = Entry(window, justify="center")
                c2 = Entry(window, justify="center")
                c3 = Entry(window, justify="center")
                c1.grid(row=2,column=0)
                c2.grid(row=2,column=1)
                c3.grid(row=2,column=2)
                c1.insert(0, x[0])
                c2.insert(0,x[1])
                c3.insert(0, x[2])
                c1.config(state='readonly')
                c2.config(state='readonly')
                c3.config(state='readonly')

        buff_foot = Label(window)
        buff_foot.grid(row=(len(results) + 2), columnspan=2)

if __name__ == '__main__':

    root = Tk()
    gui = gui(root)
    root.mainloop()
