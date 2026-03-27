import cv2
import numpy as np
def slice_image(image_path, rows, cols):
    
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image")
        return None, None
        
    h,w,_ = img.shape
    #rows = 3
    #cols = 3

    piece_h = h // rows
    piece_w = w // cols

    pieces = []
    indices = []
    for i in range(rows):
        for j in range(cols):
            piece = img[i*piece_h:(i+1)*piece_h,j*piece_w:(j+1)*piece_w]
            
            pieces.append(piece)
            indices.append(len(indices))

    print("Total pieces:", len(pieces))
    return pieces,indices

# #reconstructing form list to img

# row1 = np.hstack(pieces[0:3])
# row2 = np.hstack(pieces[3:6])
# row3 = np.hstack(pieces[6:9])

# puzzle = np.vstack((row1, row2, row3))

# cv2.imshow("Puzzle", puzzle)
# cv2.waitKey(0)
# cv2.destroyAllWindows()