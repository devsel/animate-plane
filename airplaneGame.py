
import pygame
import sys

# ------------------------
# Initialize Pygame
# ------------------------
pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Plane")

clock = pygame.time.Clock()

# ------------------------
# Colors
# ------------------------
SKY = (135, 206, 235)
WHITE = (255, 255, 255)
RED = (220, 50, 50)

# ------------------------
# Plane
# ------------------------
plane_x = 100
plane_y = 300

plane_speed = 5

# ------------------------
# Clouds
# ------------------------
clouds = [
    [700, 100],
    [900, 250],
    [1200, 180]
]

# ------------------------
# Font
# ------------------------
font = pygame.font.SysFont("Arial", 24)

# ------------------------
# Game Loop
# ------------------------
running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ------------------------
    # Keyboard
    # ------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        plane_y -= plane_speed

    if keys[pygame.K_DOWN]:
        plane_y += plane_speed

    if keys[pygame.K_LEFT]:
        plane_x -= plane_speed

    if keys[pygame.K_RIGHT]:
        plane_x += plane_speed

    # Keep plane on screen
    plane_x = max(0, min(WIDTH - 60, plane_x))
    plane_y = max(0, min(HEIGHT - 30, plane_y))

    # ------------------------
    # Move Clouds
    # ------------------------

    for cloud in clouds:

        cloud[0] -= 2

        if cloud[0] < -100:
            cloud[0] = WIDTH + 100

    # ------------------------
    # Draw
    # ------------------------

    screen.fill(SKY)

    # Clouds
    for cloud in clouds:

        pygame.draw.ellipse(screen, WHITE, (cloud[0], cloud[1], 70, 40))
        pygame.draw.ellipse(screen, WHITE, (cloud[0]+25, cloud[1]-10, 60, 45))
        pygame.draw.ellipse(screen, WHITE, (cloud[0]+50, cloud[1], 70, 40))

    # Plane body
    pygame.draw.rect(screen, RED, (plane_x, plane_y, 60, 20))

    # Nose
    pygame.draw.polygon(
        screen,
        RED,
        [
            (plane_x+60, plane_y+10),
            (plane_x+75, plane_y+20),
            (plane_x+60, plane_y)
        ]
    )

    # Wing
    pygame.draw.polygon(
        screen,
        RED,
        [
            (plane_x+20, plane_y+10),
            (plane_x+35, plane_y-10),
            (plane_x+45, plane_y+10)
        ]
    )

    # Tail
    pygame.draw.polygon(
        screen,
        RED,
        [
            (plane_x, plane_y),
            (plane_x-10, plane_y-15),
            (plane_x+10, plane_y)
        ]
    )

    text = font.render("Arrow Keys to Fly", True, (0,0,0))
    screen.blit(text, (20,20))

    pygame.display.flip()

pygame.quit()
sys.exit()
