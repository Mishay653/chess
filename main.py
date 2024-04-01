import pygame
import os

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Шахматное поле')

# Определение цветов
white = (238, 238, 210)
black = (118, 150, 86)

cell_size = width // 8

piece_images = {
    'wp': pygame.transform.scale(pygame.image.load('pieces/wpawn.png'), (cell_size, cell_size)),
    'wr': pygame.transform.scale(pygame.image.load('pieces/wrook.png'), (cell_size, cell_size)),
    'wn': pygame.transform.scale(pygame.image.load('pieces/wknight.png'), (cell_size, cell_size)),
    'wb': pygame.transform.scale(pygame.image.load('pieces/wbishop.png'), (cell_size, cell_size)),
    'wq': pygame.transform.scale(pygame.image.load('pieces/wqueen.png'), (cell_size, cell_size)),
    'wk': pygame.transform.scale(pygame.image.load('pieces/wking.png'), (cell_size, cell_size)),
    'bp': pygame.transform.scale(pygame.image.load('pieces/bpawn.png'), (cell_size, cell_size)),
    'br': pygame.transform.scale(pygame.image.load('pieces/brook.png'), (cell_size, cell_size)),
    'bn': pygame.transform.scale(pygame.image.load('pieces/bknight.png'), (cell_size, cell_size)),
    'bb': pygame.transform.scale(pygame.image.load('pieces/bbishop.png'), (cell_size, cell_size)),
    'bq': pygame.transform.scale(pygame.image.load('pieces/bqueen.png'), (cell_size, cell_size)),
    'bk': pygame.transform.scale(pygame.image.load('pieces/bking.png'), (cell_size, cell_size))
}


def draw_chess_board():
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = white
            else:
                color = black
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))


def draw_chess_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != '-':
                piece_image = piece_images[piece]
                screen.blit(piece_image, (col * cell_size, row * cell_size))


def mouse_to_board_pos(x, y):
    row = y // cell_size
    col = x // cell_size
    return row, col


selected_piece = None
selected_row = -1
selected_col = -1


def is_valid_move(board, start_row, start_col, end_row, end_col):
    piece = board[start_row][start_col]
    color = piece[0]
    if piece == 'wp':
        if end_col == start_col and end_row == start_row - 1 and board[end_row][end_col] == '-':
            return True
        elif start_row == 6 and end_col == start_col and end_row == start_row - 2 and board[end_row][end_col] == '-' and \
                board[end_row + 1][end_col] == '-':
            return True
        elif abs(end_col - start_col) == 1 and end_row == start_row - 1 and board[end_row][end_col] != '-' and \
                board[end_row][end_col][0] == 'b':
            return True
        else:
            return False
    elif piece == 'bp':
        if end_col == start_col and end_row == start_row + 1 and board[end_row][end_col] == '-':
            return True
        elif start_row == 1 and end_col == start_col and end_row == start_row + 2 and board[end_row][end_col] == '-' and \
                board[end_row - 1][end_col] == '-':
            return True
        elif abs(end_col - start_col) == 1 and end_row == start_row + 1 and board[end_row][end_col] != '-' and \
                board[end_row][end_col][0] == 'w':
            return True
        else:
            return False
    elif piece[1] == 'r':
        if start_row == end_row:
            if start_col < end_col:
                for col in range(start_col + 1, end_col):
                    if board[start_row][col] != '-' and col != end_col:
                        return False
                    elif board[start_row][col] != '-' and col == end_col and board[start_row][col][0] == piece[0]:
                        return False
                return True
            elif start_col > end_col:
                for col in range(end_col + 1, start_col):
                    if board[start_row][col] != '-' and col != end_col:
                        return False
                    elif board[start_row][col] != '-' and col == end_col and board[start_row][col][0] == piece[0]:
                        return False
                return True
        elif start_col == end_col:
            if start_row < end_row:
                for row in range(start_row + 1, end_row):
                    if board[row][start_col] != '-' and row != end_row:
                        return False
                    elif board[row][start_col] != '-' and row == end_row and board[row][start_col][0] == piece[0]:
                        return False
                return True
            elif start_row > end_row:
                for row in range(end_row + 1, start_row):
                    if board[row][start_col] != '-' and row != end_row:
                        return False
                    elif board[row][start_col] != '-' and row == end_row and board[row][start_col][0] == piece[0]:
                        return False
                return True
        else:
            return False

    elif piece[1] == 'q':
        if start_row == end_row:
            if start_col < end_col:
                for col in range(start_col + 1, end_col):
                    if board[start_row][col] != '-':
                        return False
                return True
            elif start_col > end_col:
                for col in range(end_col + 1, start_col):
                    if board[start_row][col] != '-':
                        return False
                return True
        elif start_col == end_col:
            if start_row < end_row:
                for row in range(start_row + 1, end_row):
                    if board[row][start_col] != '-':
                        return False
                return True
            elif start_row > end_row:
                for row in range(end_row + 1, start_row):
                    if board[row][start_col] != '-':
                        return False
                return True
        elif abs(start_row - end_row) == abs(start_col - end_col):
            delta_row = 1 if end_row > start_row else -1
            delta_col = 1 if end_col > start_col else -1
            row, col = start_row + delta_row, start_col + delta_col
            while row != end_row and col != end_col:
                if board[row][col] != '-':
                    return False
                row += delta_row
                col += delta_col
            return True
        else:
            return False
    elif piece[1] == 'b':
        if abs(start_row - end_row) == abs(start_col - end_col):
            delta_row = 1 if end_row > start_row else -1
            delta_col = 1 if end_col > start_col else -1
            row, col = start_row + delta_row, start_col + delta_col
            while row != end_row and col != end_col:
                if board[row][col] != '-':
                    return False
                row += delta_row
                col += delta_col
            return True
        else:
            return False
    elif piece[1] == 'n':
        if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or \
                (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2):
            return True
        else:
            return False
    elif piece[1] == 'k':
        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            return True
        if color == 'w':
            if start_col == 7 and start_row == 4 and board[7][5] == board[7][6] == '-' and board[7][7] == 'wr' \
            and (end_row == 7 and end_col == 6) or (end_row == 7 and end_col == 7):
                if start_col != end_col and start_row != end_row:
                    return True
    else:
        return False


running = True
board = [
    ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            os.system("python ui.py")
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = mouse_to_board_pos(x, y)
            if selected_piece is None:
                piece = board[row][col]
                if piece != '-':
                    selected_piece = piece
                    selected_row = row
                    selected_col = col
            else:
                if is_valid_move(board, selected_row, selected_col, row, col):
                    board[row][col] = selected_piece
                    board[selected_row][selected_col] = '-'
                selected_piece = None
                selected_row = -1
                selected_col = -1

    screen.fill(white)
    draw_chess_board()
    draw_chess_pieces(board)
    if selected_piece is not None:
        piece_image = piece_images[selected_piece]
        screen.blit(piece_image, (x - cell_size // 2, y - cell_size // 2))
    pygame.display.flip()

pygame.quit()