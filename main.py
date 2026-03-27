import pygame
from input import capture_snapshot
from generatingpuzzle import generate_puzzle
from game import start_game

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Live Puzzle")

font = pygame.font.SysFont(None, 40)

def draw_text(text, x, y):
    img = font.render(text, True, (255,255,255))
    screen.blit(img, (x,y))

state = "menu"
running = True
camera_done = False
start_time = 0
final_time = 0
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if state == "menu":

                if event.key == pygame.K_s:
                    state = "camera"

                if event.key == pygame.K_q:
                    running = False

            elif state == "instructions":
                if event.key == pygame.K_RETURN:
                    start_time = pygame.time.get_ticks()
                    state = "puzzle"
            elif state == "complete_image":
                if event.key == pygame.K_RETURN:
                    state = "solved"

            elif state == "solved":
                if event.key == pygame.K_r:
                    state = "menu"
                    camera_done = False
                if event.key == pygame.K_q:
                    running = False
    screen.fill((0,0,0))
    if state == "menu":

            draw_text("WELCOME TO LIVE PUZZLE", 120,200)
            draw_text("Press S to take snapshot", 150,260)
            draw_text("Press Q to quit", 200,300)

    elif state =="camera":

        if not camera_done:

            capture_snapshot()
            camera_done = True
            state = "loading"

    elif state == "loading":


        draw_text("Generating Puzzle.......",200,280)
        pygame.display.update()

        pygame.time.delay(1000)

        rows = 3
        cols = 3

        puzzle_image, pieces, indices, correct_order = generate_puzzle("snapshot.jpg", rows, cols)

        state = "instructions"

    elif state == "instructions":

        draw_text("HOW TO PLAY",230,180)
        draw_text("Click two tiles to swap them",140,240)
        draw_text("Solve the puzzle to win!",160,280)
        draw_text("Press ENTER to start",180,340)

    elif state == "puzzle":

        solved = start_game(pieces, indices, correct_order, rows, cols)
        if solved:

            final_time = (pygame.time.get_ticks() - start_time) // 1000
            state = "complete_image"

    elif state == "complete_image":
        img = pygame.image.load("snapshot.jpg")
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        screen.blit(img, (0,0))

        draw_text("Puzzle Completed!",180,30)
        draw_text(f"Time Taken: {final_time} seconds",150,300)
        draw_text("Press ENTER",220,70)

    elif state == "solved":

        draw_text("CONGRATULATIONS!!!",180,250)
        draw_text("You solved the puzzle!",170,300)
        draw_text("Press R to Restart",190,330)
        draw_text("Press Q to Quit",210,370)
        pygame.display.update()

    pygame.display.update()

pygame.quit()