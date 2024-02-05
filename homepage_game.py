# homepage_mc.py

import pygame
import sys
from marketplace_mc import marketplace_screen
from settings_mc import settings_screen
from world_selection import world_selection_screen

def main_menu():
    pygame.init()

    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Minecraft 2.0 - Main Menu")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Menu options
    menu_options = ["Play", "Marketplace", "Settings", "Exit"]
    selected_option = 0

    # Main loop for the main menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)

                elif event.key == pygame.K_RETURN:
                    selected_menu = menu_options[selected_option]

                    if selected_menu == "Play":
                        print("Opening Play menu...")
                        # Add logic to transition to the play menu
                        play_menu()

                    elif selected_menu == "Marketplace":
                        print("Opening Marketplace!")
                        # Add logic to transition to the marketplace screen
                        marketplace_screen(["Item 1", "Item 2", "Item 3"])

                    elif selected_menu == "Settings":
                        print("Opening Settings!")
                        # Add logic to transition to the settings screen
                        settings_screen()

                    elif selected_menu == "Exit":
                        pygame.quit()
                        sys.exit()

        # Display menu options
        screen.fill(black)
        for i, option in enumerate(menu_options):
            text_color = white if i == selected_option else (200, 200, 200)
            text = font.render(option, True, text_color)
            text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
            screen.blit(text, text_rect)
        pygame.display.flip()

def play_menu():
    pygame.init()

    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Minecraft 2.0 - Play Menu")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Play menu options
    play_menu_options = ["Start a World", "Load World", "Back"]
    selected_option = 0

    # Main loop for the play menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(play_menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(play_menu_options)

                elif event.key == pygame.K_RETURN:
                    selected_play_option = play_menu_options[selected_option]

                    if selected_play_option == "Start a World":
                        print("Starting a new world...")
                        # Add logic for starting a new world
                        # You can call a function or transition to the world creation screen

                    elif selected_play_option == "Load World":
                        print("Loading saved worlds...")
                        # Add logic for loading saved worlds
                        # You can call a function or transition to the world selection screen

                    elif selected_play_option == "Back":
                        print("Going back to the main menu!")
                        return  # Return to the main menu

        # Display play menu options
        screen.fill(black)
        for i, option in enumerate(play_menu_options):
            text_color = white if i == selected_option else (200, 200, 200)
            text = font.render(option, True, text_color)
            text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
            screen.blit(text, text_rect)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
