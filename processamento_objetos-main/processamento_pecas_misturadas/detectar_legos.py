import cv2
import numpy as np

# Carregar a imagem de teste
img = cv2.imread("lego_teste1.jpg")

# Redimensionar a imagem para facilitar o processamento (opcional)
new_size = (640, 480)
resize = cv2.resize(img, new_size)

# Converter para o espaço de cor HSV
img_hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

# Criar máscaras para cada cor (ajustar os valores HSV se necessário)
red_mask = cv2.inRange(img_hsv, (170, 210, 200), (180, 255, 255))  # Vermelho 
green_mask = cv2.inRange(img_hsv, (35, 100, 100), (85, 255, 255))  # Verde
purple_mask = cv2.inRange(img_hsv, (130, 50, 50), (150, 255, 255))  # Roxo
pink_mask = cv2.inRange(img_hsv, (160, 180, 200), (170, 255, 255)) # Rosa
blue_mask = cv2.inRange(img_hsv, (95, 240, 200), (100, 255, 255)) #Azul
white_mask = cv2.inRange(img_hsv, (0, 0, 200), (180, 50, 255))  # Branco



# Aplicar operações morfológicas para melhorar as máscaras
kernel = np.ones((5, 5), np.uint8)
red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
purple_mask = cv2.morphologyEx(purple_mask, cv2.MORPH_OPEN, kernel)
pink_mask = cv2.morphologyEx(pink_mask, cv2.MORPH_OPEN, kernel)
white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)

# Processamento de dilatação e erosão para as máscara
red_erode = cv2.erode(red_mask, kernel, iterations=1)
red_dilate = cv2.dilate(red_erode, kernel, iterations=1)
blue_erode = cv2.erode(blue_mask, kernel, iterations=1)
blue_dilate = cv2.dilate(blue_erode, kernel, iterations=1)
green_erode = cv2.erode(green_mask, kernel, iterations=1)
green_dilate = cv2.dilate(green_erode, kernel, iterations=1)
purple_erode = cv2.erode(purple_mask, kernel, iterations=1)
purple_dilate = cv2.dilate(purple_erode, kernel, iterations=1)
pink_erode = cv2.erode(pink_mask, kernel, iterations=1)
pink_dilate = cv2.dilate(pink_erode, kernel, iterations=1)
white_erode = cv2.erode(white_mask, kernel, iterations=1)
white_dilate = cv2.dilate(white_erode, kernel, iterations=1)


# Detectar contornos e desenhá-los na imagem original
def detectar_contornos(mask, color):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 400:  # Ignorar contornos muito pequenos
            cv2.drawContours(resize, [contour], -1, color, 2)

# Aplicar a detecção de contornos para cada cor
detectar_contornos(red_mask, (0, 0, 255))  # Vermelho
detectar_contornos(green_mask, (0, 255, 0))  # Verde
detectar_contornos(purple_mask, (128, 0, 128))  # Roxo
detectar_contornos(pink_mask, (255, 105, 180))  # Rosa
detectar_contornos(blue_mask, (255, 0, 0))  # Azul
detectar_contornos(white_mask, (255, 255, 255))  # Branco

# Achando os contornos das peças de Lego conforme as máscaras de cores e escrevendo a quantidade na imagem
cont = 0
name = ["azul", "verde", "branco", "vermelho", "roxo", "rosa"]
color = [(255, 0, 0), (0, 255, 0), (255, 255, 255), (0, 0, 255), (128, 0, 128), (255, 105, 180)]
array = [blue_mask, green_mask, white_mask, red_mask, purple_mask, pink_mask]

for i in range(len(array)):
    qtd = 0
    contornos, hierarquia = cv2.findContours(array[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for x in range(len(contornos)):
        area = cv2.contourArea(contornos[x])
        # Filtrar objetos pequenos
        if area > 400:
            # Desenhar os contornos
            cv2.drawContours(resize, contornos, x, color[i], 2)
            qtd += 1
    # Escrever a quantidade na imagem
    cv2.putText(resize, name[i] + ": " + str(qtd), (10 + cont, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color[i], 1, cv2.LINE_AA)
    cont += 100  # Incrementar posição horizontal para exibir os textos lado a lado

# Exibir a imagem processada
#cv2.imshow("Peças de Lego Detectadas", resize)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Exibir máscaras intermediárias
#cv2.imshow("Máscara Vermelha", white_mask)
#cv2.imshow("Imagem Pós Erosion", white_erode)
#cv2.imshow("Imagem Pós Dilation", white_dilate)
cv2.waitKey(0)  # Espera até uma tecla ser pressionada para continuar
cv2.destroyAllWindows()
