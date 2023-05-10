#function to prevent the window from moving on refresh
def UpdateWindowLocation(UI):
    UI.windowLocation[0],UI.windowLocation[1]=UI.winfo_x(),UI.winfo_y()
    return UI.windowLocation