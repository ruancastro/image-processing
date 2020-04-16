import numpy as np 
import cv2
import argparse

import src.R_G_B as rgb
import src.Img_Colorida as imcolor 
import src.img_borrada  as imborr
import src.Threshold as bin 
import src.Edge_detection as edg
import src.countours as ct


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])


# # Mostrando a imagem dividida em (R G e B).
# # Press 'esc' para sair ou press 's' para salvar as imagens
# rgb.exibe_rgb(image)

# # Mostrando a imagem colorida (R G e B). 
# # Press 'esc' para sair ou press 's' para salvar as imagens
# imcolor.imagem_colorida(image)

# # Borrando a imagem  
# imborr.borrar_img(image,2) 

# # Binarizando a imagem
# bin.binarizar_imagem(image)

# # Detecção de borda da imagem
# edg.edge_detect(image,1)

# Definindo os contornos da imagem
ct.def_contornos(image,1)
