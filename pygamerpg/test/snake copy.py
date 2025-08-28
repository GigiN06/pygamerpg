import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caesar Cipher Typing (Shift +3)")

# Set up font
font = pygame.font.Font(None, 48)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Text storage
input_text = ""

# Caesar cipher shift function
def shift_letter(char, shift=3):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                input_text += '\n'
            else:
                input_text += shift_letter(event.unicode)

    # Render text
    text_surface = font.render(input_text, True, BLACK)
    win.blit(text_surface, (20, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
