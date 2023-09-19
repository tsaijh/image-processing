import cvzone
import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation

#path = r'C:\Users\TSAI\Desktop\human.jpg'
#path = r'C:\Users\TSAI\Desktop\Chevy 4L60E Two Piece Green Plug No Top Bolt 2WD BACK.jpg'
#path = r'C:\Users\TSAI\Desktop\Chevy 4L60E Two Piece Green Plug No Top Bolt 2WD TOP.jpg'
path = r'C:\Users\TSAI\Desktop\Chevy 4L60E Two Piece Green Plug No Top Bolt 2WD 2WD BOTTOM.jpg'

segmentor = SelfiSegmentation()
img = cv2.imread(path)
img_Out = segmentor.removeBG(img, (255,255,255), threshold=0.1)

cv2.imwrite(r'C:\Users\TSAI\Desktop\fgbg2.jpg', img_Out)