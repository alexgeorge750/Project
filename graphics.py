import pygame
import sys

# Initialize pygame
pygame.init()

# Use this to set up the display
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Haunted Mansion Adventure")


font = pygame.font.SysFont("Times New Roman", 40)

background_image = pygame.Surface((screen_width, screen_height))
background_image.fill((0, 0, 0))

title_text = font.render("Welcome to the Haunted Mansion!", True, (250, 250, 250))
instructions_text = font.render("Press any key to start the game...", True, (250, 250, 250))

def show_opening_screen():
    """Function to display the opening screen"""
    screen.blit(background_image, (1, 1))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 3))
    screen.blit(instructions_text, (screen_width // 2 - instructions_text.get_width() // 2, screen_height // 2))

    pygame.display.update()

    # Wait for the player to press any key to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Start the game when a key is pressed
                waiting = False

# Show the opening screen
show_opening_screen()

# Initialize the game (text-based part)
print('''Welcome to the haunted mansion text-based adventure game! In this  
game, you have stumbled upon a haunted mansion one night, and you decide  
to go explore. Can you make it out alive? Type your character's name below 
to start!''')

player_name = input('>>')
current_player = Player((2,1), player_name, 5, [])

print("Your current location is: " + current_location.description)

run_game()
