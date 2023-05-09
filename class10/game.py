#cmd 에서 별도 설치
#pip install pygame

import pygame
import random

pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("장애물 피하기 게임")

icon_width = 50
icon_height = 50
icon_color = (255, 255, 255)

icon_position = pygame.math.Vector2(screen_width / 2 - icon_width / 2, screen_height / 2 - icon_height / 2)

icon_speed = pygame.math.Vector2(0,0)

obstacle_width = 50
obstacle_height = 50
obstacle_color = (255, 255, 0)
obstacle_count = 5
obstacles = []

for _ in range(obstacle_count):
    obstacles.append(pygame.math.Vector2(
        random.randint(0, screen_width - obstacle_width),
        random.randint(-obstacle_height * 2, -obstacle_height)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        icon_speed.x = 0.3 * (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        icon_speed.y = 0.3 * (keys[pygame.K_DOWN] - keys[pygame.K_UP])
        
        for obs in obstacles:
            obs.y += 0.2

            if obs.y > screen_height :
                obs.x = random.randint(0, screen_width - obstacle_width)
                obs.y - random.randint(-obstacle_width * 2, -obstacle_width)

        icon_rect = pygame.Rect(icon_position.x, icon_position.y, icon_width, icon_height)

        for obs in obstacles:
            obstacle_rect = pygame.Rect(obs.x, obs.y, obstacle_width, obstacle_height)
            if icon_rect.colliderect(obstacle_rect):
                print("게임 오버")
                running = False
        
        #화면 표시
        screen.fill((0,0,0))
        pygame.draw.rect(screen, icon_color, pygame.Rect(icon_position.x, icon_position.y, icon_width, icon_height))
        for obs in obstacles:
            pygame.draw.rect(screen, icon_color, pygame.Rect(obs.x, obs.y, obstacle_width, obstacle_height))
        pygame.display.flip()

pygame.quit()

icon_position += icon_speed
icon_position.x = max(min(icon_position.x, screen_width - icon_width), 0)
icon_position.y = max(min(icon_position.y, screen_height - icon_height), 0)
