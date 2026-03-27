import random
import cv2
import numpy as np
from imgslicing import slice_image

def generate_puzzle(image_path,rows,cols):
    #rows = 3
    #cols = 3

    # get pieces from slicing file
    pieces, indices = slice_image(image_path, rows, cols)

    # shuffling puzzle pieces
    combined = list(zip(pieces, indices))
    random.shuffle(combined)

    pieces, indices = zip(*combined)

    pieces = list(pieces)
    indices = list(indices)

    #reconstructing form list to img

    puzzle_rows = []
    for i in range(rows):
            row = np.hstack(pieces[i*cols:(i+1)*cols])
            puzzle_rows.append(row)

    puzzle_image = np.vstack(puzzle_rows)

    correct_order = list(range(rows*cols))

    return puzzle_image,pieces,indices,correct_order