import pygame
import cv2

pygame.init()

WIDTH = 600
HEIGHT = 600

def numpy_to_surface(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_rgb = img_rgb.swapaxes(0, 1)

    surface = pygame.surfarray.make_surface(img_rgb)

    return surface
def start_game(pieces,indices,correct_order,rows,cols):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))#creation of game window
    pygame.display.set_caption("Puzzle Game")

    tile_size = WIDTH // cols
    tiles = [] 
    for piece in pieces:
        piece = cv2.resize(piece, (tile_size, tile_size))
        tiles.append(numpy_to_surface(piece))

    running = True
    selected_tile = None
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return False       

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col_clicked = mouse_x // tile_size
                row_clicked = mouse_y // tile_size
                tile_index = row_clicked * cols + col_clicked
                print("Clicked tile:", tile_index)

                if selected_tile is None:
                    selected_tile = tile_index
                    print("First tile:", selected_tile)

                else:
                    print("Second tile:", tile_index)

                    # swap tiles
                    tiles[selected_tile], tiles[tile_index] = (tiles[tile_index], tiles[selected_tile],)
                     # swap indices 
                    indices[selected_tile], indices[tile_index] = (indices[tile_index], indices[selected_tile],)

                    selected_tile = None
                    if indices == correct_order:
                        print("PUZZLE SOLVED!!!!")
                        return True
        screen.fill((0,0,0))

        for i in range(len(tiles)):
            row = i // cols
            col = i % cols

            x = col * tile_size
            y = row * tile_size

            screen.blit(tiles[i], (x,y))
            # draw grid border
            pygame.draw.rect(screen, (255,255,255), (x,y,tile_size,tile_size), 2)

            # highlight selected tile
            if selected_tile == i:
                pygame.draw.rect(screen, (255,0,0), (x,y,tile_size,tile_size), 4)
        pygame.display.update()

    pygame.quit()