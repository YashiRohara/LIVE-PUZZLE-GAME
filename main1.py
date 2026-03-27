# import cv2
# img = cv2.imread("document\pic.jpg",0)
# # -1 or cv2.IMREAD_COLOR = loads clour image i.e ingores transparency
# # 0 or cv2.IMREAD_grayscale = loads in greyscale
# # 1 or cv2.IMREAD_unchanged = loads as it is
# #img = cv2.resize(img,(400,400))
# # or
# img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
# img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite('new_img.jpg',img)
# cv2.imshow('yashi',img)
# cv2.waitKey(0) #0 for infinity & anynumber for that millisecond
# cv2.destroyAllWindows()