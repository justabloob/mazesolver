from graphics import Window, Point, Line

def main():
    # create the window
    window = Window(800, 600)
    # create a line
    line = Line(Point(100, 100), Point(200, 200))
    # draw a line
    window.draw_line(line, "black")
    # wait for the window to close
    window.wait_for_close()


if __name__ == "__main__":
    main()