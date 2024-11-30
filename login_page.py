# login_page.py

import pygame
from database import Database

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.SysFont('Arial', 30)

# Create the login screen
def login_screen(screen):
    # Create a new surface for the login page
    screen.fill(WHITE)
    
    # Display a title
    title_text = font.render('Enter Your Information', True, BLACK)
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))

    # Render input fields
    name_text = font.render('Name:', True, BLACK)
    screen.blit(name_text, (150, 150))

    age_text = font.render('Age:', True, BLACK)
    screen.blit(age_text, (150, 200))

    # Create input boxes (Here you can just draw rectangles for now)
    pygame.draw.rect(screen, BLACK, (300, 150, 200, 40), 2)
    pygame.draw.rect(screen, BLACK, (300, 200, 200, 40), 2)

    # Input fields for name and age
    player_name = ''
    player_age = ''

    active_name = False
    active_age = False

    name_input_box = pygame.Rect(300, 150, 200, 40)
    age_input_box = pygame.Rect(300, 200, 200, 40)

    # Initialize database
    db = Database()

    # Event loop for login page
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if active_name:
                    if event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode
                if active_age:
                    if event.key == pygame.K_BACKSPACE:
                        player_age = player_age[:-1]
                    else:
                        player_age += event.unicode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if name_input_box.collidepoint(event.pos):
                    active_name = True
                    active_age = False
                elif age_input_box.collidepoint(event.pos):
                    active_age = True
                    active_name = False

        # Display the name and age input fields
        name_text_input = font.render(player_name, True, BLACK)
        screen.blit(name_text_input, (name_input_box.x + 5, name_input_box.y + 5))
        
        age_text_input = font.render(player_age, True, BLACK)
        screen.blit(age_text_input, (age_input_box.x + 5, age_input_box.y + 5))

        # Add a submit button
        submit_button = pygame.Rect(screen.get_width() // 2 - 100, 300, 200, 50)
        pygame.draw.rect(screen, GREEN, submit_button)
        submit_text = font.render('Start Game', True, WHITE)
        screen.blit(submit_text, (submit_button.x + 60, submit_button.y + 10))

        # Check if the submit button is clicked
        if pygame.mouse.get_pressed()[0]:
            if submit_button.collidepoint(pygame.mouse.get_pos()):
                # Store player data in the database
                db.save_player_data(player_name, player_age)
                running = False

        # Update the screen
        pygame.display.update()
