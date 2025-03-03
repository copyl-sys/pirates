#!/usr/bin/env python3
"""
Pirate Latitudes: A Reimagined Epic Adventure
Inspired by *Pirate Latitudes* by Michael Crichton.
All rights to the original text and story belong to Michael Crichton and his estate.

This interactive text adventure combines a choose‐your‐own‐adventure narrative with a Zork-style command input.
With multiple branches, puzzles, and encounters, this experience is designed to fill over two hours of gameplay.
"""

import sys
import time

def pause():
    """Small pause to enhance dramatic effect."""
    time.sleep(1.5)

def slow_print(text):
    """Print text with a slight delay for atmosphere."""
    for line in text.split("\n"):
        print(line)
        time.sleep(1)
    print()

def show_intro():
    slow_print(r"""
     ____  _                 _       _       _      _       
    |  _ \| | __ _ _ __   __| | ___ | |__   | |    / \   ___ ___ ___
    | |_) | |/ _` | '_ \ / _` |/ _ \| '_ \  | |   / _ \ / __/ __/ _ \
    |  __/| | (_| | | | | (_| | (_) | |_) | | |  / ___ \ (_| (_|  __/
    |_|   |_|\__,_|_| |_|\__,_|\___/|_.__/  |_| /_/   \_\___\___\___/

    Welcome, daring adventurer, to a reimagined journey of piracy and mystery!
    
    Inspired by Michael Crichton’s *Pirate Latitudes*, this epic adventure plunges you
    into a world of swashbuckling intrigue, secret islands, and hidden treasures.
    
    All rights to the original work belong to Michael Crichton and his estate.
    Prepare to carve your legend upon the digital seas and through forgotten isles.
    """)
    print("Type 'help' at any time to see the available commands.\n")
    pause()


def help_menu():
    print("\nAvailable commands:")
    print("  look            - Observe your surroundings")
    print("  examine         - Get more details about an object or location")
    print("  north/south/east/west - Move in a direction")
    print("  sail            - Set sail to a new destination")
    print("  board           - Board a ship or enter a location")
    print("  search/read     - Look for clues or treasure")
    print("  fight           - Engage in battle")
    print("  negotiate       - Attempt to parley with others")
    print("  unlock          - Try to open a locked object or passage")
    print("  help            - Show this help menu")
    print("  quit            - Exit the adventure\n")


def scene_ship_deck():
    slow_print("\n--- The Ship's Deck ---")
    slow_print("You stand on the weather-beaten deck of the pirate ship 'The Black Meridian.'")
    slow_print("The salty air and creaking wood recall tales of daring escapades and lost treasure.")
    slow_print("A tattered map and a captain's log rest on a barrel near the helm, hinting at secrets of a hidden island fortress.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("You observe the lively crew, swaying masts, and the mysterious map that seems to hold a clue to an ancient treasure.")
        elif cmd in ["sail"]:
            slow_print("You command the helmsman to set a course into the unknown. The ship lurches forward into the deep blue.")
            pause()
            scene_open_sea()
            break
        elif cmd in ["board"]:
            slow_print("You decide to venture below deck where whispers of hidden clues and secret meetings stir.")
            pause()
            scene_below_deck()
            break
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("The tides recede as you exit the adventure. Farewell, brave pirate!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for available commands.")


def scene_below_deck():
    slow_print("\n--- Below Deck ---")
    slow_print("The narrow corridors beneath the ship reveal a world of dim lanterns and hushed voices.")
    slow_print("You find a worn journal containing cryptic notes and sketches of a secret island fortress.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("The journal's pages detail hidden coves, rival pirate factions, and strange symbols that seem like a map.")
        elif cmd in ["search", "read"]:
            slow_print("Decoding the journal's cryptic entries, you learn of an island shrouded in mystery—its fortress guarding unimaginable treasures.")
            pause()
            scene_crew_quarters()
            break
        elif cmd in ["sail"]:
            slow_print("Believing the clues are sufficient, you hurry back to the deck to set sail towards the island.")
            pause()
            scene_open_sea()
            break
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("Retreating from the secrets below deck, you end your adventure. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for guidance.")


def scene_crew_quarters():
    slow_print("\n--- Crew Quarters ---")
    slow_print("In the bustling crew quarters, voices murmur about a mysterious advisor rumored to know the island’s true secrets.")
    slow_print("A grizzled sailor with a cybernetic eye catches your attention.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("You notice faded portraits of legendary pirates and a map pinned to the wall with annotated routes.")
        elif cmd in ["talk", "negotiate"]:
            slow_print("You approach the sailor, who introduces himself as 'Old Byte'. He offers to share his knowledge—for a price.")
            slow_print("He speaks of a rival pirate captain who has recently secured part of the treasure map. Do you:")
            slow_print("  1. Trade some of your own clues for his insights?")
            slow_print("  2. Threaten him for the information?")
            choice = input("Choose 1 or 2: ").strip()
            if choice == "1":
                slow_print("Old Byte nods and reveals that the map leads to a series of puzzles scattered across the island.")
                pause()
                scene_open_sea()
                break
            elif choice == "2":
                slow_print("The sailor recoils in anger and warns you against rash decisions. The mood in the quarters sours.")
                slow_print("Realizing you might have lost a valuable ally, you decide to return to the deck.")
                pause()
                scene_ship_deck()
                break
            else:
                slow_print("Uncertain, you hesitate and the moment slips away.")
        elif cmd in ["sail"]:
            slow_print("You decide not to delay any longer and return to the deck to set sail for the island.")
            pause()
            scene_open_sea()
            break
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("Leaving the crew quarters, you step away from the hidden secrets. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for available commands.")


def scene_open_sea():
    slow_print("\n--- Open Sea ---")
    slow_print("The ship cuts through the waves as dark clouds gather overhead.")
    slow_print("A violent storm brews on the horizon, and the whispered promises of treasure drive you onward.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("The sea is restless, with turbulent waves and flashes of lightning that mirror your inner conflict.")
        elif cmd in ["sail"]:
            slow_print("You steer the ship into the heart of the storm. The winds howl and the deck becomes a chaotic battleground.")
            pause()
            scene_storm_at_sea()
            break
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("Unable to face the storm, you choose to abandon your quest. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' to see your options.")


def scene_storm_at_sea():
    slow_print("\n--- Storm at Sea ---")
    slow_print("Rain lashes the deck and thunder shakes the very timbers of the ship.")
    slow_print("Amid the chaos, you must make split-second decisions to survive the fury of nature.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("The deck is slippery, crew members scramble for safety, and a sense of dread fills the air.")
        elif cmd in ["fight"]:
            slow_print("You rally a group of loyal crew to secure the rigging and fend off the chaotic elements.")
            slow_print("After a grueling struggle, you manage to steady the ship. The storm begins to subside.")
            pause()
            scene_island_approach()
            break
        elif cmd in ["negotiate", "help"]:
            slow_print("You shout orders, coordinating the crew to weather the storm through sheer determination.")
            slow_print("Gradually, your leadership and quick thinking pull everyone to safety as the storm fades.")
            pause()
            scene_island_approach()
            break
        elif cmd in ["quit", "exit"]:
            slow_print("The storm proves too much, and you abandon ship. Your adventure ends here.")
            sys.exit(0)
        else:
            slow_print("Command not recognized. In the midst of the tempest, you must act swiftly!")


def scene_island_approach():
    slow_print("\n--- Approach to the Secret Island ---")
    slow_print("After battling the storm, the skies clear to reveal a blood-red sunset.")
    slow_print("In the distance, a dark silhouette emerges—a rugged island with steep cliffs and hidden fortifications.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("From the deck, you discern cannons, watchtowers, and a network of secret coves etched into the rocky shoreline.")
        elif cmd in ["board", "land"]:
            slow_print("You lower the boats and prepare a landing party. The island’s mysteries beckon.")
            pause()
            scene_island_forest()
            break
        elif cmd in ["sail"]:
            slow_print("You hesitate, watching the island for further clues, until a sudden flash of light compels you to act.")
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("You decide the island's perils are too great and retreat from the quest. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for available commands.")


def scene_island_forest():
    slow_print("\n--- The Island Jungle ---")
    slow_print("Stepping onto the island, you find yourself in a dense jungle alive with mysterious sounds and shifting shadows.")
    slow_print("Ancient stone markers and cryptic carvings hint at a civilization long past—and a treasure yet undiscovered.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("Towering trees and tangled undergrowth surround you, with moss-covered relics peeking through.")
        elif cmd in ["search", "explore"]:
            slow_print("Venturing deeper, you discover a bifurcation: one path leads to an abandoned village, the other to a rocky outcrop that appears to be a lookout.")
            slow_print("Do you choose to go to the village (type 'village') or the lookout (type 'lookout')?")
            choice = input(">> ").lower().strip()
            if choice == "village":
                pause()
                scene_abandoned_village()
                break
            elif choice == "lookout":
                pause()
                scene_lookout()
                break
            else:
                slow_print("That path is unclear. Choose 'village' or 'lookout'.")
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("The jungle swallows your footsteps as you abandon your quest. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for guidance.")


def scene_abandoned_village():
    slow_print("\n--- Abandoned Village ---")
    slow_print("You enter a ghostly village where time seems to stand still. Crumbling huts and faded murals depict the island’s storied past.")
    slow_print("In the center, a stone pedestal holds a fragmented piece of an ancient treasure map.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("The murals tell tales of epic sea battles and secret alliances. The pedestal seems to beckon you closer.")
        elif cmd in ["search", "read"]:
            slow_print("You carefully piece together the fragments of the map, revealing coordinates and clues to the fortress hidden deep within the island.")
            pause()
            scene_rival_encounter()
            break
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("Haunted by memories of the past, you decide to leave the village behind. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for available commands.")


def scene_lookout():
    slow_print("\n--- Rocky Lookout ---")
    slow_print("Climbing the rugged outcrop, you reach a natural lookout with a panoramic view of the island.")
    slow_print("Below, you see a fortified structure surrounded by lush jungles—a potential treasure vault or a trap laid by rival pirates.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("The structure is ancient yet formidable. You can almost sense the weight of untold secrets within its walls.")
        elif cmd in ["search"]:
            slow_print("You discover a hidden inscription carved into the rock. It warns of betrayal and hints at a secret entrance accessible only by solving a riddle.")
            slow_print("The riddle reads: 'I am not alive, yet I grow; I don't have lungs, yet I need air; What am I?'")
            answer = input("Your answer: ").lower().strip()
            if "fire" in answer:
                slow_print("Correct! A hidden passage opens behind a curtain of vines.")
                pause()
                scene_fortress()
                break
            else:
                slow_print("That is not the answer. The inscription remains silent. Perhaps try again or choose another path.")
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("The isolation of the lookout proves too daunting and you descend in defeat. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for guidance.")


def scene_rival_encounter():
    slow_print("\n--- Rival Pirate Encounter ---")
    slow_print("As you leave the abandoned village, a sleek, modern skiff appears on the horizon.")
    slow_print("A notorious rival pirate captain, known as 'Crimson Byte', challenges you for the secrets of the map.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("Crimson Byte's crew are armed with futuristic gadgets and a fierce determination to claim the treasure for themselves.")
        elif cmd in ["fight"]:
            slow_print("A clash ensues! Amid clashing steel and bursts of digital sparks, you engage in a heated duel.")
            slow_print("After an intense battle, you defeat Crimson Byte and secure your path forward, though you bear scars as proof of the encounter.")
            pause()
            scene_fortress()
            break
        elif cmd in ["negotiate"]:
            slow_print("You attempt a parley with Crimson Byte, offering a share of future riches in exchange for safe passage.")
            slow_print("After tense negotiations, he begrudgingly agrees to a temporary alliance. But trust is fragile on these waters.")
            pause()
            scene_fortress()
            break
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("Overwhelmed by the confrontation, you decide to retreat. Your adventure ends here.")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for available commands.")


def scene_fortress():
    slow_print("\n--- The Island Fortress ---")
    slow_print("You arrive at a looming fortress carved into the side of a rugged cliff.")
    slow_print("Ancient stone walls, partly overgrown with vines, hide secret chambers and traps that have foiled many before you.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("You see intricate carvings, locked gates, and a subtle glimmer from behind a heavy door—perhaps the treasure vault lies beyond.")
        elif cmd in ["unlock"]:
            slow_print("You examine the door closely and discover it is secured with a complex mechanism.")
            slow_print("Using clues from the map and inscriptions you gathered, you attempt to unlock it.")
            pause()
            slow_print("After a tense few moments, the lock clicks open, revealing a dark passage.")
            scene_treasure_vault()
            break
        elif cmd in ["fight"]:
            slow_print("Suddenly, defenders of the fortress emerge from hidden alcoves!")
            slow_print("You engage in a fierce battle. After a challenging fight, you force your way past them.")
            pause()
            slow_print("Exhausted but determined, you approach the locked door.")
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("Overcome by the fortress's perils, you decide to abandon your quest. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for available commands.")


def scene_treasure_vault():
    slow_print("\n--- The Treasure Vault ---")
    slow_print("Beyond the unlocked door, you step into a chamber glittering with riches.")
    slow_print("Ancient coins, dazzling jewels, and mysterious artifacts fill the vault. But more than wealth, this treasure tells the island’s history.")
    
    while True:
        cmd = input(">> ").lower().strip()
        if cmd in ["look", "examine"]:
            slow_print("Every artifact and relic here whispers a tale of epic sea battles, secret alliances, and lost civilizations.")
        elif cmd in ["search", "read"]:
            slow_print("Among the treasures, you find a final journal that recounts the legacy of the island and the true meaning behind the treasure.")
            slow_print("Your name will now be etched in pirate lore as one who unlocked the secrets of the island!")
            slow_print("Congratulations, brave adventurer, on completing your quest!")
            pause()
            scene_final()
            break
        elif cmd in ["help"]:
            help_menu()
        elif cmd in ["quit", "exit"]:
            slow_print("Leaving behind the legacy of the treasure vault, you sail into history. Farewell!")
            sys.exit(0)
        else:
            slow_print("Command not recognized. Try 'help' for available commands.")


def scene_final():
    slow_print("\n--- Epilogue ---")
    slow_print("As the sun rises over the horizon, the island fades into legend.")
    slow_print("The choices you made and the battles you fought have secured your place among the great pirates of history.")
    slow_print("Your adventure may end here, but the tales of your exploits will be told for generations to come.")
    slow_print("Thank you for playing this homage to *Pirate Latitudes* by Michael Crichton!")
    sys.exit(0)


def main():
    show_intro()
    help_menu()
    # Begin the adventure on the ship's deck
    scene_ship_deck()


if __name__ == "__main__":
    main()
