import requests
import cv2
import numpy as np

url = "https://tse4.mm.bing.net/th?id=OIP.PYipJ_hSncugM2SwnZitvgHaEK&pid=Api&P=0"

while True:
    cam = requests.get(url)
    imgNp = np.array(bytearray(cam.content), dtype=np.uint8)
    img = cv2.imdecode(imgNp, 1)
    cv2.imshow("cam", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
