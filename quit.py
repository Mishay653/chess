import pygame
import sys
import os

# Цвета
BACKGROUND_COLOR = (50, 50, 50)
BUTTON_COLOR = (255, 255, 255)


def main():
    # Инициализация Pygame
    pygame.init()

    # Размер окна
    width, height = 640, 480

    # Создание окна
    screen = pygame.display.set_mode((width, height))

    # Загрузка шрифта
    font = pygame.font.Font("freesansbold.ttf", 20)

    # Текст вопроса
    text = font.render("Вы действительно хотите выйти из игры?", True, BUTTON_COLOR)

    # Создание кнопок
    button_width, button_height = 100, 50
    yes_button = pygame.Rect(width // 2 - button_width - 50, height // 2 + 50, button_width, button_height)
    no_button = pygame.Rect(width // 2 + 50, height // 2 + 50, button_width, button_height)

    # Цикл обработки событий
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            # Закрытие окна
            if event.type == pygame.QUIT:
                sys.exit()

            # Нажатие кнопки
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Выход из игры
                if yes_button.collidepoint(event.pos):
                    # Закрытие окна
                    pygame.quit()

                    # Закрытие main.py
                    os.system("taskkill /f /im main.py")
                    running = False
                    pygame.quit()
                    sys.exit()

                # Отмена
                elif no_button.collidepoint(event.pos):
                    running = False

        # Отрисовка
        screen.fill(BACKGROUND_COLOR)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 50))

        # Кнопки
        pygame.draw.rect(screen, BUTTON_COLOR, yes_button)
        pygame.draw.rect(screen, BUTTON_COLOR, no_button)

        # Текст кнопок
        yes_text = font.render("Да", True, (0, 0, 0))
        no_text = font.render("Нет", True, (0, 0, 0))
        screen.blit(yes_text, (yes_button.x + button_width // 2 - yes_text.get_width() // 2,
                               yes_button.y + button_height // 2 - yes_text.get_height() // 2))
        screen.blit(no_text, (no_button.x + button_width // 2 - no_text.get_width() // 2,
                              no_button.y + button_height // 2 - no_text.get_height() // 2))

        # Обновление экрана
        pygame.display.update()


if __name__ == "__main__":
    main()