from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        # create the rootg widget
        self.__root = Tk()
        # set title
        self.__root.title("My window")
        #create canvas widget
        self.__canvas = Canvas(self.__root, width=width, height=height)
        #pack the canvas
        self.__canvas.pack(fill=BOTH, expand=1)
        # set running state
        self.__running = False
        #add protocol for closing window
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
        self.__root.quit()
        self.__root.destroy()