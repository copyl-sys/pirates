#!/usr/bin/env python3
"""
Pirate Latitudes: Ultimate Curses Enhanced Epic Adventure with ASCII Movies
Inspired by *Pirate Latitudes* by Michael Crichton.
All rights to the original text and story belong to Michael Crichton and his estate.

This version extends the curses UI to include an ASCII intro movie and an ending ASCII movie.
"""

import curses
import time
import json
import os
import random
import signal

SAVE_FILE = "pirate_latitudes_save.json"

# Global game state
game_state = {
    "current_scene": "intro",
    "name": "Captain Anonymous",
    "inventory": [],
    "health": 100,
    "skills": {"combat": 5, "negotiation": 3, "puzzle": 4},
    "reputation": 0,
    "achievements": [],
    "story_log": []
}

############################
# Curses UI Layout Setup
############################

def init_windows(stdscr):
    """Divide the screen into header, main, sidebar, input, and footer windows."""
    height, width = stdscr.getmaxyx()
    
    header_height = 3
    input_height = 3
    footer_height = 1
    sidebar_width = 40

    main_height = height - header_height - input_height - footer_height
    main_width = width - sidebar_width

    header_win = curses.newwin(header_height, width, 0, 0)
    main_win = curses.newwin(main_height, main_width, header_height, 0)
    sidebar_win = curses.newwin(main_height, sidebar_width, header_height, main_width)
    input_win = curses.newwin(input_height, width, header_height + main_height, 0)
    footer_win = curses.newwin(footer_height, width, height - footer_height, 0)

    main_win.scrollok(True)
    return header_win, main_win, sidebar_win, input_win, footer_win

def update_header(header_win):
    """Update the header bar with game title and status info."""
    header_win.clear()
    title = "Pirate Latitudes: Ultimate Epic Adventure"
    status = f"Health: {game_state['health']}  Reputation: {game_state['reputation']}"
    header_win.addstr(0, 2, title, curses.A_BOLD)
    header_win.addstr(1, 2, status)
    header_win.hline(2, 0, curses.ACS_HLINE, header_win.getmaxyx()[1])
    header_win.refresh()

def update_footer(footer_win):
    """Update the footer bar (for hints or extra info)."""
    footer_win.clear()
    footer_win.addstr(0, 2, "Type 'help' for commands. ")
    footer_win.refresh()

def update_sidebar(sidebar_win):
    """Display an ASCII map in the sidebar window."""
    sidebar_win.clear()
    ascii_map = (
        " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
        " |         SEA OF MYSTERY        |\n"
        " |   [Ship Deck] --- [Open Sea]    |\n"
        " |         |                     |\n"
        " |   [Below Deck] --- [Crew Qtrs]  |\n"
        " |                             |\n"
        " |  [Island Approach] --- [Jungle]|\n"
        " |                             |\n"
        " |   [Fortress] --- [Treasure]   |\n"
        " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n"
    )
    sidebar_win.addstr(0, 0, ascii_map)
    sidebar_win.box()
    sidebar_win.refresh()

def curses_slow_print(win, text, delay=0.05):
    """Print text to the given window slowly (character-by-character)."""
    for ch in text:
        win.addstr(ch)
        win.refresh()
        time.sleep(delay)
    win.addstr("\n")
    win.refresh()

def curses_get_input(win, prompt=">> "):
    """Display a prompt in the input window and return the user's input."""
    win.clear()
    win.addstr(0, 0, prompt)
    win.refresh()
    curses.echo()
    inp = win.getstr().decode("utf-8")
    curses.noecho()
    return inp.strip()

############################
# ASCII Intro Movie
############################

def ascii_intro_movie(stdscr):
    """Display a series of ASCII art frames as an intro movie."""
    frames = [
r"""
   _____  _           _        _      _ 
  |  __ \| |         | |      | |    | |
  | |__) | |__   __ _| |_ __ _| | ___| |
  |  ___/| '_ \ / _` | __/ _` | |/ _ \ |
  | |    | | | | (_| | || (_| | |  __/_|
  |_|    |_| |_|\__,_|\__\__,_|_|\___(_)

         ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
       ~       PIRATE LATITUDES        ~
         ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
""",
r"""
         _________
        /         \
       /  PIRATE   \
      |  LATITUDES  |
       \           /
        \_________/
    
         ~  ~  ~  ~  ~  ~ 
       ~  Welcome Aboard  ~
         ~  ~  ~  ~  ~  ~ 
""",
r"""
              |    |    |
             )_)  )_)  )_)
            )___))___))___)\
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
"""
    ]
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for frame in frames:
        stdscr.clear()
        lines = frame.splitlines()
        start_y = (height - len(lines)) // 2
        for i, line in enumerate(lines):
            x = max((width - len(line)) // 2, 0)
            stdscr.addstr(start_y + i, x, line)
        stdscr.refresh()
        time.sleep(2)
    stdscr.clear()
    stdscr.refresh()

############################
# ASCII Ending Movie
############################

def ascii_ending_movie(stdscr):
    """Display a series of ASCII art frames as an ending movie."""
    frames = [
r"""
          _______
         /       \
        |  THE    |
        |  END    |
         \_______/
""",
r"""
        ~~~~~~~~~~~~~~~~~~~~
       ~   Farewell, brave   ~
       ~       pirate!       ~
        ~~~~~~~~~~~~~~~~~~~~
""",
r"""
        ~  ~  ~  ~  ~  ~  ~  ~
     ~                       ~
   ~  THE JOURNEY LIVES ON!    ~
     ~                       ~
        ~  ~  ~  ~  ~  ~  ~  ~
"""
    ]
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for frame in frames:
        stdscr.clear()
        lines = frame.splitlines()
        start_y = (height - len(lines)) // 2
        for i, line in enumerate(lines):
            x = max((width - len(line)) // 2, 0)
            stdscr.addstr(start_y + i, x, line)
        stdscr.refresh()
        time.sleep(2)
    stdscr.clear()
    stdscr.addstr(height//2, (width-20)//2, "Thank you for playing!")
    stdscr.refresh()
    time.sleep(3)

############################
# Save/Load Functions
############################

def save_game():
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(game_state, f)
        return "Game saved successfully!"
    except Exception as e:
        return f"Failed to save game: {e}"

def load_game():
    global game_state
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                game_state = json.load(f)
            return "Game loaded successfully!"
        except Exception as e:
            return f"Failed to load game: {e}"
    else:
        return "No save file found."

############################
# Command Parser
############################

def parse_command(user_input):
    commands = {
        "look": ["look", "examine", "view"],
        "sail": ["sail", "navigate", "set course"],
        "board": ["board", "enter"],
        "search": ["search", "read", "investigate"],
        "fight": ["fight", "attack", "duel"],
        "negotiate": ["negotiate", "talk", "parley"],
        "unlock": ["unlock", "open"],
        "map": ["map", "show map"],
        "journal": ["journal", "codex"],
        "help": ["help", "commands"],
        "quit": ["quit", "exit"],
        "save": ["save"],
        "load": ["load"]
    }
    for cmd, synonyms in commands.items():
        for synonym in synonyms:
            if user_input.startswith(synonym):
                return cmd
    return user_input.split()[0]

############################
# In-Game Journal Functions
############################

def add_event(event):
    game_state["story_log"].append(event)

def display_journal(main_win):
    main_win.clear()
    main_win.addstr("=== In-Game Journal ===\n", curses.A_BOLD)
    if game_state["story_log"]:
        for event in game_state["story_log"]:
            main_win.addstr(f" * {event}\n")
    else:
        main_win.addstr("No events logged yet.\n")
    main_win.addstr("\nPress any key to continue...")
    main_win.refresh()
    main_win.getch()

############################
# Sample Scene Functions
############################

def scene_ship_deck(header_win, main_win, sidebar_win, input_win, footer_win):
    game_state["current_scene"] = "ship_deck"
    add_event("Arrived at the Ship's Deck.")
    main_win.clear()
    curses_slow_print(main_win, f"{game_state['name']}, you stand on the weather-beaten deck of 'The Black Meridian'.")
    curses_slow_print(main_win, "A tattered map and a captain's log hint at secrets of a hidden island fortress.")
    update_sidebar(sidebar_win)
    update_header(header_win)
    update_footer(footer_win)
    
    while True:
        user_input = curses_get_input(input_win)
        cmd = parse_command(user_input.lower().strip())
        if cmd == "look":
            curses_slow_print(main_win, "You see a bustling deck with crew members and a mysterious map.")
        elif cmd == "sail":
            curses_slow_print(main_win, "You command the helmsman to set sail into the deep blue.")
            scene_open_sea(header_win, main_win, sidebar_win, input_win, footer_win)
            break
        elif cmd == "board":
            curses_slow_print(main_win, "You venture below deck, where whispered secrets abound.")
            scene_below_deck(header_win, main_win, sidebar_win, input_win, footer_win)
            break
        elif cmd == "map":
            update_sidebar(sidebar_win)
        elif cmd == "save":
            msg = save_game()
            curses_slow_print(main_win, msg)
        elif cmd == "load":
            msg = load_game()
            curses_slow_print(main_win, msg)
        elif cmd == "journal":
            display_journal(main_win)
        elif cmd == "quit":
            curses_slow_print(main_win, "The tides recede as you exit the adventure. Farewell!")
            exit(0)
        elif cmd == "help":
            display_help_menu(main_win, input_win)
        else:
            curses_slow_print(main_win, "Command not recognized. Try 'help'.")

def scene_below_deck(header_win, main_win, sidebar_win, input_win, footer_win):
    game_state["current_scene"] = "below_deck"
    add_event("Exploring Below Deck.")
    main_win.clear()
    curses_slow_print(main_win, "In the cramped corridors beneath the ship, dim lanterns reveal a weathered journal.")
    update_sidebar(sidebar_win)
    update_header(header_win)
    update_footer(footer_win)
    
    while True:
        user_input = curses_get_input(input_win)
        cmd = parse_command(user_input.lower().strip())
        if cmd == "look":
            curses_slow_print(main_win, "The journal details hidden coves and mysterious symbols.")
        elif cmd == "search":
            curses_slow_print(main_win, "Decoding the entries, you learn of an island fortress with untold treasures.")
            add_event("Learned about secret island.")
            scene_ship_deck(header_win, main_win, sidebar_win, input_win, footer_win)
            break
        elif cmd == "sail":
            curses_slow_print(main_win, "Believing the clues suffice, you return to the deck to set sail.")
            scene_ship_deck(header_win, main_win, sidebar_win, input_win, footer_win)
            break
        elif cmd == "map":
            update_sidebar(sidebar_win)
        elif cmd == "save":
            msg = save_game()
            curses_slow_print(main_win, msg)
        elif cmd == "load":
            msg = load_game()
            curses_slow_print(main_win, msg)
        elif cmd == "journal":
            display_journal(main_win)
        elif cmd == "quit":
            curses_slow_print(main_win, "Retreating from below deck, you end your adventure. Farewell!")
            exit(0)
        elif cmd == "help":
            display_help_menu(main_win, input_win)
        else:
            curses_slow_print(main_win, "Command not recognized. Try 'help'.")

def scene_open_sea(header_win, main_win, sidebar_win, input_win, footer_win):
    game_state["current_scene"] = "open_sea"
    add_event("Sailing on the Open Sea.")
    main_win.clear()
    curses_slow_print(main_win, "The ship cuts through restless waves as dark clouds gather overhead.")
    update_sidebar(sidebar_win)
    update_header(header_win)
    update_footer(footer_win)
    
    while True:
        user_input = curses_get_input(input_win)
        cmd = parse_command(user_input.lower().strip())
        if cmd == "look":
            curses_slow_print(main_win, "Turbulent waves and flashes of lightning mirror your inner turmoil.")
        elif cmd == "sail":
            curses_slow_print(main_win, "You steer the ship into the heart of the storm. The winds howl!")
            scene_storm_at_sea(header_win, main_win, sidebar_win, input_win, footer_win)
            break
        elif cmd == "map":
            update_sidebar(sidebar_win)
        elif cmd == "save":
            msg = save_game()
            curses_slow_print(main_win, msg)
        elif cmd == "load":
            msg = load_game()
            curses_slow_print(main_win, msg)
        elif cmd == "journal":
            display_journal(main_win)
        elif cmd == "quit":
            curses_slow_print(main_win, "Unable to face the storm, you abandon your quest. Farewell!")
            exit(0)
        elif cmd == "help":
            display_help_menu(main_win, input_win)
        else:
            curses_slow_print(main_win, "Command not recognized. Try 'help'.")

def scene_storm_at_sea(header_win, main_win, sidebar_win, input_win, footer_win):
    game_state["current_scene"] = "storm_at_sea"
    add_event("Endured the Storm at Sea.")
    main_win.clear()
    curses_slow_print(main_win, "Rain lashes the deck and thunder shakes the ship. The storm is fierce!")
    update_sidebar(sidebar_win)
    update_header(header_win)
    update_footer(footer_win)
    
    while True:
        user_input = curses_get_input(input_win)
        cmd = parse_command(user_input.lower().strip())
        if cmd == "look":
            curses_slow_print(main_win, "The deck is slippery and the crew scrambles in the tempest.")
        elif cmd == "fight":
            curses_slow_print(main_win, "You rally your crew to secure the ship.")
            if game_state["skills"]["combat"] + random.randint(0, 3) > 6:
                curses_slow_print(main_win, "Your skill prevails! The storm begins to subside.")
                add_event("Conquered the storm.")
                scene_island_approach(header_win, main_win, sidebar_win, input_win, footer_win)
                break
            else:
                curses_slow_print(main_win, "The storm takes its toll. You lose 15 health.")
                game_state["health"] -= 15
                if game_state["health"] <= 0:
                    curses_slow_print(main_win, "You have succumbed to the storm...")
                    exit(0)
                scene_island_approach(header_win, main_win, sidebar_win, input_win, footer_win)
                break
        elif cmd == "negotiate":
            curses_slow_print(main_win, "You shout orders and inspire your crew with a rousing shanty. The tempest abates.")
            scene_island_approach(header_win, main_win, sidebar_win, input_win, footer_win)
            break
        elif cmd == "map":
            update_sidebar(sidebar_win)
        elif cmd == "save":
            msg = save_game()
            curses_slow_print(main_win, msg)
        elif cmd == "load":
            msg = load_game()
            curses_slow_print(main_win, msg)
        elif cmd == "quit":
            curses_slow_print(main_win, "The storm overwhelms you, and you abandon ship. Farewell!")
            exit(0)
        elif cmd == "help":
            display_help_menu(main_win, input_win)
        else:
            curses_slow_print(main_win, "Command not recognized. Act swiftly!")

def scene_island_approach(header_win, main_win, sidebar_win, input_win, footer_win):
    game_state["current_scene"] = "island_approach"
    add_event("Approaching the Secret Island.")
    main_win.clear()
    curses_slow_print(main_win, "After the storm, a blood‑red sunset reveals a rugged island with hidden fortifications.")
    update_sidebar(sidebar_win)
    update_header(header_win)
    update_footer(footer_win)
    
    while True:
        user_input = curses_get_input(input_win)
        cmd = parse_command(user_input.lower().strip())
        if cmd == "look":
            curses_slow_print(main_win, "From the deck, you see cannons, watchtowers, and secret coves carved into the rocks.")
        elif cmd == "board":
            curses_slow_print(main_win, "You lower the boats and prepare a landing party.")
            scene_ship_deck(header_win, main_win, sidebar_win, input_win, footer_win)
            break
        elif cmd == "map":
            update_sidebar(sidebar_win)
        elif cmd == "save":
            msg = save_game()
            curses_slow_print(main_win, msg)
        elif cmd == "load":
            msg = load_game()
            curses_slow_print(main_win, msg)
        elif cmd == "quit":
            curses_slow_print(main_win, "Fearing the island's perils, you retreat. Farewell!")
            exit(0)
        elif cmd == "help":
            display_help_menu(main_win, input_win)
        else:
            curses_slow_print(main_win, "Command not recognized. Try 'help'.")

############################
# Help Menu Display
############################

def display_help_menu(main_win, input_win):
    help_text = (
        "Help / Commands:\n"
        "  look/examine/view      - Observe your surroundings\n"
        "  sail/navigate/set course - Set sail to a new destination\n"
        "  board/enter             - Board a ship or enter a location\n"
        "  search/read/investigate - Look for clues or treasure\n"
        "  fight/attack/duel       - Engage in battle\n"
        "  negotiate/talk/parley   - Parley with others\n"
        "  unlock/open             - Open a locked door\n"
        "  map/show map            - Display the ASCII map\n"
        "  journal/codex           - Show your in-game journal\n"
        "  save                    - Save your progress\n"
        "  load                    - Load your progress\n"
        "  help/commands           - Show this help menu\n"
        "  quit/exit               - Exit the adventure\n\n"
        "Press any key to return..."
    )
    main_win.clear()
    curses_slow_print(main_win, help_text, delay=0.02)
    input_win.clear()
    input_win.addstr(0, 0, "Press any key to continue...")
    input_win.refresh()
    input_win.getch()

############################
# Main Curses Function
############################

def curses_main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    # Show ASCII Intro Movie
    ascii_intro_movie(stdscr)
    
    header_win, main_win, sidebar_win, input_win, footer_win = init_windows(stdscr)
    
    while True:
        # Main Menu Loop
        header_win.clear()
        main_menu_items = ["New Game", "Load Game", "Help", "Quit"]
        selection = 0
        while True:
            header_win.clear()
            height, width = header_win.getmaxyx()
            title = "Pirate Latitudes: Ultimate Epic Adventure"
            header_win.addstr(0, (width - len(title)) // 2, title, curses.A_BOLD)
            for idx, item in enumerate(main_menu_items):
                x = (width - len(item)) // 2
                y = 1 + idx
                if idx == selection:
                    header_win.attron(curses.A_REVERSE)
                    header_win.addstr(y, x, item)
                    header_win.attroff(curses.A_REVERSE)
                else:
                    header_win.addstr(y, x, item)
            header_win.refresh()
            key = stdscr.getch()
            if key == curses.KEY_UP:
                selection = (selection - 1) % len(main_menu_items)
            elif key == curses.KEY_DOWN:
                selection = (selection + 1) % len(main_menu_items)
            elif key in [10, 13]:
                break

        choice = main_menu_items[selection]
        if choice == "New Game":
            # Character customization then start at ship deck
            character_customization(stdscr)
            scene_ship_deck(header_win, main_win, sidebar_win, input_win, footer_win)
        elif choice == "Load Game":
            msg = load_game()
            main_win.clear()
            curses_slow_print(main_win, msg)
            main_win.addstr("\nPress any key to continue...")
            main_win.refresh()
            main_win.getch()
            scene_ship_deck(header_win, main_win, sidebar_win, input_win, footer_win)
        elif choice == "Help":
            display_help_menu(main_win, input_win)
        elif choice == "Quit":
            main_win.clear()
            main_win.addstr("Farewell, brave pirate!\n")
            main_win.refresh()
            time.sleep(2)
            break

    # After game loop, show the ending movie.
    ascii_ending_movie(stdscr)

if __name__ == "__main__":
    curses.wrapper(curses_main)
