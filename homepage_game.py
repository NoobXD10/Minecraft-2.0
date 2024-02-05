import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minecraft 2.0")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create a font object
font = pygame.font.Font(None, 36)

# Menu options
menu_options = ["Play", "Marketplace", "Settings"]
selected_option = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle arrow key navigation
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)

            # Pressing Enter for the selected option
            elif event.key == pygame.K_RETURN:
                selected_menu = menu_options[selected_option]
                print(f"Selected: {selected_menu}")

    # Clear the screen
    screen.fill(black)

    # Draw menu options
    for i, option in enumerate(menu_options):
        text_color = white if i == selected_option else (200, 200, 200)
        text = font.render(option, True, text_color)
        text_rect = text.get_rect(center=(width // 2, height // 2 + i * 50))
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

