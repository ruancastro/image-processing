import cv2
import numpy as np 

    
def def_contornos(image,fator_de_reduc=1):

    img_redim = cv2.resize(image, None, fx = 1/fator_de_reduc, fy = 1/fator_de_reduc, interpolation = cv2.INTER_AREA)

    gray = cv2.cvtColor(img_redim, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    cv2.imshow("Image", img_redim)
    edged = cv2.Canny(blurred, 30, 150)
    cv2.imshow("Edges", edged)
    

    # aux_img = canny
    # aux_name = 'Canny'

    (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # print("I count {} coins in this image".format(len(cnts)))
    coins = image.copy()
    cv2.drawContours(coins, cnts, -1, (0, 255, 0), 1)
    cv2.imshow("Coins", coins)
    
    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif ord('s'):
        cv2.imwrite("output/Contornada_pintada.png",coins)
        cv2.imwrite("output/Contornada.png",edged)



    # k = cv2.waitKey()
    # if k==27:
    #     cv2.destroyAllWindows()
    # elif ord('s'):
    #     cv2.imwrite('')