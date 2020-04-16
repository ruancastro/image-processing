# Formally, edge detection embodies mathematical methods to find points in an image where the
# brightness of pixel intensities changes distinctly.

import cv2
import numpy as np

def edge_detect(image,fator_de_reduc=1) :

    img_redim = cv2.resize(image, None, fx = 1/fator_de_reduc, fy = 1/fator_de_reduc, interpolation = cv2.INTER_AREA)
    
    img_redim = cv2.cvtColor(img_redim, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", image)
    

    # Laplaciano 
    # lap = cv2.Laplacian(img_redim, cv2.CV_64F)
    # lap = np.uint8(np.absolute(lap))
    # cv2.imshow("Laplacian", lap)
    # aux_img = lap
    # aux_name = 'laplaciano' 

    # # Laplacian and sobel
    # # Aqui, a imagem parece ser um pouco mais real, não há traços "fortes" das bordas tanto quanto o  modelo canny.

    # sobelX = cv2.Sobel(img_redim, cv2.CV_64F, 1, 0)
    # sobelY = cv2.Sobel(img_redim, cv2.CV_64F, 0, 1)
    # sobelX = np.uint8(np.absolute(sobelX))
    # sobelY = np.uint8(np.absolute(sobelY))
    # sobelCombined = cv2.bitwise_or(sobelX, sobelY)
    # cv2.imshow("Sobel X", sobelX)
    # cv2.imshow("Sobel Y", sobelY)
    # cv2.imshow("Sobel_Combined", sobelCombined)

    # aux_img = sobelCombined
    # aux_name = 'Sobel Combined'

    # canny edge detector
    # Nesse tipo, temos uma borda mais nítida do que quando aplicamos aplenas o laplaciano ou o laplaciano com o sobel
    # Todavia, há um parâmetro humano que é a definição dos limiares (30 e 150)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("Blurred", img_redim)
    canny = cv2.Canny(img_redim, 30, 150)
    # values below 30 are considered non-edges whereas any values above 150 are considered edges.
    cv2.imshow("Canny", canny)
    cv2.waitKey(0)
    aux_img = canny
    aux_name = 'Canny'


    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('output/Edge_detect_{}.png'.format(aux_name),aux_img)