import pygame, sys
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((550,550))
pygame.display.set_caption("Tic Tac Toe")
board = [0,0,0],[0,0,0],[0,0,0]

def win_check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2-tile] == num:
            continue
        else:
            break
    else:
        return True


first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150))  # color and location and size
second = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150))
third = pygame.draw.rect(win, (255, 255, 255), (375, 25, 150, 150))

fourth = pygame.draw.rect(win, (255, 255, 255), (25, 200, 150, 150))  # color and location and size
fifth = pygame.draw.rect(win, (255, 255, 255), (200, 200, 150, 150))
sixth = pygame.draw.rect(win, (255, 255, 255), (375, 200, 150, 150))

seventh = pygame.draw.rect(win, (255, 255, 255), (25, 375, 150, 150))  # color and location and size
eighth = pygame.draw.rect(win, (255, 255, 255), (200, 375, 150, 150))
ninth = pygame.draw.rect(win, (255, 255, 255), (375, 375, 150, 150))
#def gameUpdate():  # this can be used to display game
 #   while True:
  #      for event in pygame.event.get():
   #            pygame.quit()
    #            sys.exit()
     #   pygame.display.update()
#gameUpdate()
run = True
draw_obj = 'rect'
first_reserved = True
second_reserved = True
third_reserved = True
fourth_reserved = True
fifth_reserved = True
sixth_reserved = True
seventh_reserved = True
eighth_reserved = True
ninth_reserved = True

won = False

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                won = False
                run = True
                board = [0,0,0],[0,0,0],[0,0,0]
                first_reserved = True
                second_reserved = True
                third_reserved = True
                fourth_reserved = True
                fifth_reserved = True
                sixth_reserved = True
                seventh_reserved = True
                eighth_reserved = True
                ninth_reserved = True
                first = pygame.draw.rect(win, (255, 255, 255), (25, 25, 150, 150))  # color and location and size
                second = pygame.draw.rect(win, (255, 255, 255), (200, 25, 150, 150))
                third = pygame.draw.rect(win, (255, 255, 255), (375, 25, 150, 150))

                fourth = pygame.draw.rect(win, (255, 255, 255), (25, 200, 150, 150))  # color and location and size
                fifth = pygame.draw.rect(win, (255, 255, 255), (200, 200, 150, 150))
                sixth = pygame.draw.rect(win, (255, 255, 255), (375, 200, 150, 150))

                seventh = pygame.draw.rect(win, (255, 255, 255), (25, 375, 150, 150))  # color and location and size
                eighth = pygame.draw.rect(win, (255, 255, 255), (200, 375, 150, 150))
                ninth = pygame.draw.rect(win, (255, 255, 255), (375, 375, 150, 150))

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if won != True:
                if first.collidepoint(pos) and first_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (50, 50, 100, 100))
                        draw_obj = 'circle'
                        board[0][0] = 1
                        # cordinates(starting) point, margin, width,height
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (100, 100), 50)
                        draw_obj = 'rect'
                        board[0][0] = 2
                        # cordinates of straight,  cordinates of height, radius
                    first_reserved = False
                if second.collidepoint(pos) and second_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (225, 50, 100, 100))
                        draw_obj = 'circle'
                        board[0][1] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (275, 100), 50)
                        draw_obj = 'rect'
                        board[0][1] = 2
                    second_reserved = False
                if third.collidepoint(pos) and third_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (400, 50, 100, 100))
                        draw_obj = 'circle'
                        board[0][2] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (450, 100), 50)
                        draw_obj = 'rect'
                        board[0][2] = 2
                    third_reserved = False
                if fourth.collidepoint(pos) and fourth_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (50, 225, 100, 100))
                        draw_obj = 'circle'
                        board[1][0] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (100, 275), 50)
                        draw_obj = 'rect'
                        board[1][0]=2
                    fourth_reserved = False
                if fifth.collidepoint(pos) and fifth_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (225, 225, 100, 100))
                        draw_obj = 'circle'
                        board[1][1] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (275, 275), 50)
                        draw_obj = 'rect'
                        board[1][1] = 2
                    fifth_reserved = False
                if sixth.collidepoint(pos) and sixth_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (400, 225, 100, 100))
                        draw_obj = 'circle'
                        board[1][2] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (450, 275), 50)
                        draw_obj = 'rect'
                        board[1][2] = 2
                    sixth_reserved = False
                if seventh.collidepoint(pos) and seventh_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (50, 400, 100, 100))
                        draw_obj = 'circle'
                        board[2][0] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (100, 450), 50)
                        draw_obj = 'rect'
                        board[2][0] = 2
                    seventh_reserved = False
                if eighth.collidepoint(pos) and eighth_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (225, 400, 100, 100))
                        draw_obj = 'circle'
                        board[2][1] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (275, 450), 50)
                        draw_obj = 'rect'
                        board[2][1] = 2
                    eighth_reserved = False
                if ninth.collidepoint(pos) and ninth_reserved:
                    if draw_obj == 'rect':
                        pygame.draw.rect(win, (255, 0, 0), (400, 400, 100, 100))
                        draw_obj = 'circle'
                        board[2][2] = 1
                    else:
                        pygame.draw.circle(win, (0, 255, 0), (450, 450), 50)
                        draw_obj = 'rect'
                        board[2][2] = 2
                    ninth_reserved = False
        if win_check(1):
            won = True
            i = 1
            while i:
                print('red win')
                break
        elif win_check(2):
            won = True
            i = 1
            while i:
                print('green win')
                break
    pygame.display.update()
pygame.quit()
print(board)
