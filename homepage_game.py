# ... (previous code)

elif selected_menu == "Play":
    # Load play_game.py or transition to your gameplay logic
    print("Loading Play options...")

    # Display options under "Play"
    play_options = ["Start a World", "Load World", "Worlds"]
    play_selected_option = 0

    while True:
        for play_event in pygame.event.get():
            if play_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif play_event.type == pygame.KEYDOWN:
                if play_event.key == pygame.K_UP:
                    play_selected_option = (play_selected_option - 1) % len(play_options)
                elif play_event.key == pygame.K_DOWN:
                    play_selected_option = (play_selected_option + 1) % len(play_options)

                elif play_event.key == pygame.K_RETURN:
                    selected_play_option = play_options[play_selected_option]

                    if selected_play_option == "Start a World":
                        print("Starting a new world...")
                        # Add logic for starting a new world

                    elif selected_play_option == "Load World":
                        print("Loading saved worlds...")
                        # Add logic for loading saved worlds

                    elif selected_play_option == "Worlds":
                        print("Opening Worlds menu...")
                        # Add logic to transition to the world selection screen
                        from world_selection import world_selection_screen
                        world_selection_screen()

        # ... (rest of the code)
