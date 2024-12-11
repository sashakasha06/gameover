import pygame
import sys
import os

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen_width, screen_height = 600, 300
screen = pygame.display.set_mode((screen_width, screen_height))

# Установка начального цвета окна (синий)
background_color = (0, 0, 255)

# Загрузка изображения и установка его размеров
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.display.set_caption('Гейм овер')
image = load_image("gameover.png")

# Установим начальную позицию изображения
image_x = -600
image_y = 0

# Установка скорости движения изображения (пиксели в секунду)
speed = 200

# Установка времени для проверки времени цикла
clock = pygame.time.Clock()

# Основной цикл программы
running = True
while running:
    # Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Вычисление времени, прошедшего с последнего кадра
    dt = clock.tick(60) / 1000  # Время в секундах

    # Обновление позиции изображения
    if image_x < screen_width - 600:
        image_x += speed * dt

    # Отрисовка фона и изображения
    screen.fill(background_color)
    screen.blit(image, (image_x, image_y))

    # Обновление экрана
    if image_x < 0:
        pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()