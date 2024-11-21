import cv2
import numpy as np

#Script para obter o valor HSV de um pixel em uma imagem.
def obter_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = img[y, x]
        hsv_pixel = cv2.cvtColor(np.uint8([[pixel]]), cv2.COLOR_BGR2HSV)
        print(f"HSV em ({x}, {y}): {hsv_pixel[0][0]}")

img = cv2.imread("C:/Users/narki/OneDrive/teste/lego_teste1.jpg") # Substituir pelo caminho da imagem
if img is None:
    print("Erro: Imagem não encontrada. Verifique o caminho.")
else:
    print("Imagem carregada com sucesso!")
cv2.imshow("Clique para capturar HSV", img)
cv2.setMouseCallback("Clique para capturar HSV", obter_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
