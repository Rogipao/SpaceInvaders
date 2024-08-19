import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as constantes
WIDTH, HEIGHT = 640, 480
PLAYER_SIZE = 50
PLAYER_SPEED = 5
GRAVITY = 1
JUMP_HEIGHT = 20

# Define as cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Cria a janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define o jogador
player = pygame.Rect(WIDTH / 2, HEIGHT / 2, PLAYER_SIZE, PLAYER_SIZE)
player_velocity = [0, 0]

# Define o obstáculo (o barril)
obstacle = pygame.Rect(WIDTH / 2, HEIGHT / 2 + 100, 50, 50)

# Loop do jogo
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_velocity[1] = -JUMP_HEIGHT

    # Movimento do jogador
    player.x += player_velocity[0]
    player.y += player_velocity[1]

    # Aplica a gravidade
    player_velocity[1] += GRAVITY

    # Verifica colisão com o obstáculo
    if player.colliderect(obstacle):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Desenha o jogador e o obstáculo
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, RED, obstacle)

    # Atualiza a tela
    pygame.display.flip()
    pygame.time.Clock().tick(60)