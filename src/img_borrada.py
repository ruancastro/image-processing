# Pelo o que eu vi existem quatro formas comuns de borrar uma imagem : averaging, gaussian , median e bilateral
# Quando usamos o filtro gaussiano, temos uma imagem um pouco menos borrada, porém, mais natural do que
# quando utilizamos o averaging, todavia, o "median blur" é ainda mais efetivo. 
# O tipo bilateral é muito utilizado para reduzir detalhes da imagem, tende a excluir detalhes principalmente das bordas
import numpy as np
import cv2

def borrar_img(image,fator_de_reduc=1):
    
    img_redim = cv2.resize(image, None, fx = 1/fator_de_reduc, fy = 1/fator_de_reduc, interpolation = cv2.INTER_AREA)

    cv2.imshow("Original", image)
    blurred = np.hstack([
    
    # # Averaging
    # cv2.blur(img_redim, (3, 3)),
    # cv2.blur(img_redim, (5, 5)),
    # cv2.blur(img_redim, (7, 7))])
    # cv2.imshow("Averaged", blurred)
    # tipo = 'Averaged'

    # # Gaussian 
    # cv2.GaussianBlur(img_redim, (3, 3), 0),
    # cv2.GaussianBlur(img_redim, (5, 5), 0),
    # cv2.GaussianBlur(img_redim, (7, 7), 0)])
    # cv2.imshow("Gaussian", blurred)
    # tipo = 'Gaussian'
   
    # Median
    cv2.medianBlur(img_redim, 3),
    cv2.medianBlur(img_redim, 5),
    cv2.medianBlur(img_redim, 7)])
    cv2.imshow("Median", blurred)
    tipo = 'Median'

    # # bilateral 
    # cv2.bilateralFilter(img_redim, 5, 21, 21),
    # cv2.bilateralFilter(img_redim, 7, 31, 31),
    # cv2.bilateralFilter(img_redim, 9, 41, 41)])
    # cv2.imshow("Bilateral", blurred)
    # tipo = 'Bilateral'


    
    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif k==ord('s'):
       cv2.imwrite('output/Imagem_borrada_{}.png'.format(tipo),blurred)