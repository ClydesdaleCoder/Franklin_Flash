from asciimatics.screen import Screen
from time import sleep

def main():
    def start(screen):
        start.clear()
        screen.print_at('Hello! Welcome to Franklin Flash,my most recent way to use flashcards in the terminal. this is perfect wfor when you want to make studying about computers require using computers', 0, 0)
        screen.refresh()
        sleep(10)

    Screen.wrapper(start)

if __name__ == "__main__":
    main()
