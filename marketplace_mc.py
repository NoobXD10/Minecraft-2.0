# marketplace_mc.py

import pygame
import sys

def marketplace_screen(marketplace_items):
    pygame.init()

    # Set up the display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Minecraft 2.0 - Marketplace")

    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Selected item index
    selected_item = 0

    # Main loop for marketplace screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(marketplace_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(marketplace_items)

                elif event.key == pygame.K_RETURN:
                    selected_option = marketplace_items[selected_item]
                    print(f"Selected item: {selected_option}")
                    # Add logic for handling the selected marketplace item

        # Display marketplace items
        screen.fill(black)
        for i, item in enumerate(marketplace_items):
            text_color = white if i == selected_item else (200, 200, 200)
            text = font.render(item, True, text_color)
            text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
            screen.blit(text, text_rect)
        pygame.display.flip()

if __name__ == "__main__":
    # Example usage with a list of marketplace items
    example_items = ["Item A", "Item B", "Item C"]
    marketplace_screen(example_items)
