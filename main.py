from tkinter import Tk
from gui import ExpenditureManagerApp

def main():
    #Create the main application window
    root = Tk()
    
    #Initialize the Expenditure Manager application
    app = ExpenditureManagerApp(root)
    
    #Run the application's event loop
    root.mainloop()

#Start the application if this script is run directly
if __name__ == "__main__":
    main()
