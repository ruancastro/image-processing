# Normally, we use thresholding to focus on objects or areas of particular interest in an image.

import cv2 

def binarizar_imagem(image):

    
    cv2.imshow("Original", image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("Escala de cinza e borrada", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # simple thresholding 
    # Nesse tipo , precisamos estabelecer um parâmetro T , para que sirva de limiar para binarizar os píxels.
    # T = 155  " blurred, 155, 255, cv2.THRESH_BINARY"

    # (T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
    # cv2.imshow("Threshold Binary", thresh)
    # (T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("Threshold Binary Inverse", threshInv)
    # cv2.imshow("Coins", cv2.bitwise_and(image, image, mask = threshInv))
    # cv2.waitKey(0)


    # binarização "mean"
    thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
    cv2.imshow("Mean Thresh", thresh)

    # binarização "gaussiana"
    thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
    cv2.imshow("Gaussian Thresh", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()