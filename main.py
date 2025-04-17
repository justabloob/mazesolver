from window import Window

def main():
    # create the window
    window = Window(800, 600)
    # wait for the window to close
    window.wait_for_close()


if __name__ == "__main__":
    main()