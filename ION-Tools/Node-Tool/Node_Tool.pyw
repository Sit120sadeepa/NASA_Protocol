#This script is use as part of the initial loading process of the application
#Its 2 functions are to initialise the GUI and keep it running.

#Import Scripts from directory
from NT_User_Interface.NT_UI import LoadGUI

#Load Graphical Interface
GUI = LoadGUI()
GUI.mainloop()