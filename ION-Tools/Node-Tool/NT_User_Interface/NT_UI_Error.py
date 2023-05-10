import tkinter as tk

#Generic error window template.
def ErrorGUI(windowLocation,ErrorMessage):
    #Create Higher level Window
    errorWindow = tk.Toplevel()
    windowX = str(windowLocation[0]+20)
    windowY = str(windowLocation[1]+40)
    errorWindow.geometry("300x80"+"+"+windowX+"+"+windowY)
    errorWindow.title('Error')
    warningMessage = tk.Label(errorWindow, text="Error : "+ErrorMessage)
    warningMessage.pack()
    Button = tk.Button(errorWindow, width=20 ,text="Ok", command=lambda:errorWindow.destroy())
    Button.pack()
