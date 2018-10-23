import pygame
import subprocess

pygame.init()

height = 800
width = 800

screen = pygame.display.set_mode((width, height))

sky_blue = (18,178,238,100)
black = (0, 0, 0)
white = (255, 255, 255)

def displaytext(msg, color, location=(0, 0), textsize=55):
    font = pygame.font.SysFont(None, textsize)
    text = font.render(msg, True, color)
    x = font.size(msg)[0]
    y = font.size(msg)[1]
    screen.blit(text, (location[0] - x/2, location[1] - y/2))


running = True

while running:
    screen.fill(white)

    pos = pygame.mouse.get_pos()

    # Highlights the box if the cursor is inside
    if width/2 - 50 < pos[0] < width/2 + 50 and height/2 - 50 < pos[1] < height/2 + 50:
        screen.fill(sky_blue)

    displaytext("Scan", black, (width/2, height/2))

    for event in pygame.event.get():
        # Checks to see if the user clicks the X
        if event.type == pygame.QUIT:
            running = False

        # Checks to see if the user wants to exit the game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Checks to see if the user presses inside the flip button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            subprocess.call("recognize.sh", shell=True)

        pygame.display.flip()
        pygame.time.wait(15)
