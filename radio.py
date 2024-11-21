import curses
import subprocess

# Seznam rádiových stanic (jméno a URL)




stations = [
    ("RockZone", "https://icecast5.play.cz/rockzone128.mp3"),
    ("Rock Radio", "https://playerservices.streamtheworld.com/api/livestream-redirect/ROCK_RADIO_128.mp3"),
    ("Radiozurnal", "https://rozhlas.stream/radiozurnal.mp3"),
    ("Radio BOB - Symphonic metal", "https://regiocast.streamabc.net/regc-radiobobsymphmetal4646931-mp3-192-2318934"),
    ("Radio BOB - Metal", "https://streams.radiobob.de/bob-metal/mp3-128"),
    ("Radio BOB - Metalcore", "https://streams.radiobob.de/metalcore/mp3-128"),
    ("Radio BOB - Death Metal", "https://streams.radiobob.de/deathmetal/mp3-192"),
    ("Radio Bloodstream", "http://uk1.internet-radio.com:8294/stream"),
    ("Radio Metal on - The Brutal", "https://radiometalon.com:8010/radio.mp3"),
    ("Rádio Metalomanie", "https://ice.abradio.cz/metalomanie128.mp3"),
 



]

ascii_art = """
███╗   ███╗███████╗████████╗ █████╗ ██╗     
████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██║     
██╔████╔██║█████╗     ██║   ███████║██║     
██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║     
██║ ╚═╝ ██║███████╗   ██║   ██║  ██║███████╗
╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ 
           radio player 1.0
"""

def play_stream(url):
    """Spustí mpv pro přehrávání rádia"""
    subprocess.call(["mpv", url])

def main(stdscr):
    curses.curs_set(0)  # Skryje kurzor
    current_row = 0

    while True:


        stdscr.clear()

        # Vykreslení nadpisu
        for i, line in enumerate(ascii_art.strip().split("\n")):
            stdscr.addstr(i, 0, line)

            # Doplňte další text pod ASCII art
            stdscr.addstr(8, 0, "Select and ENTER for playing, Q for STOP or EXIT")
    

        # Vykreslení seznamu stanic
        for idx, (name, _) in enumerate(stations):
            if idx == current_row:
                stdscr.addstr(10 + idx, 0, name, curses.A_REVERSE)  # Zvýraznění
            else:
                stdscr.addstr(10 + idx, 0, name)

        # Získání vstupu od uživatele
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(stations) - 1:
            current_row += 1
        elif key == ord("\n"):  # Enter - přehrávání
            play_stream(stations[current_row][1])
        elif key == ord("q"):  # Q - ukončení
            break

        stdscr.refresh()

# Spuštění aplikace




curses.wrapper(main)

