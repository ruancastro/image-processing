import cv2
import numpy as np
# Colorindo as imagens, fundindo um canal com o outro todo zerado .
# O resultado é uma imagem azul, outra vede, outra vermelha .
def imagem_colorida(image):
    (B, G, R) = cv2.split(image)
    zeros = np.zeros(image.shape[:2], dtype = "uint8")
    Img_verm = cv2.merge([zeros, zeros, R])
    Img_verd = cv2.merge([zeros, G, zeros])
    Img_azul = cv2.merge([B, zeros, zeros])
    cv2.imshow("Red",Img_verm )
    cv2.imshow("Green",Img_verd)
    cv2.imshow("Blue",Img_azul )
    k = cv2.waitKey(0)

    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('output/Imagem_vermelha.png',Img_verm)
        cv2.imwrite('output/Imagem_Verde.png',Img_verd)
        cv2.imwrite('output/Imagem_Azul.png',Img_azul)   
        cv2.destroyAllWindows()