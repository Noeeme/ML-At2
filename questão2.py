import cv2
from matplotlib import pyplot as plt

image_path = "C:/Users/Noeeme/OneDrive/Imagens/image2.jpg"

image = cv2.imread(image_path)
if(image is not None) :
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    blurred_image = cv2.blur(image, (5, 5))
    processed_image = cv2.medianBlur(image, 3)
    blurred_image2 = cv2.GaussianBlur(image, (7, 7), 0)
    
def pltNormalImage():
    plt.subplot(1,2,1)
    plt.imshow(image_rgb)
    plt.title('Imagem 2d Normal')

i = 1
while i < 3 :

    if i == 1 :
        pltNormalImage()
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
        plt.title('Imagem 2d Suavizada (Filtro de Média)')
        plt.show()            
        i +=1

    if i == 2 :
        pltNormalImage()
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB))
        plt.title('Imagem 2d Suavizada (Filtro de Mediana)')
        plt.show()
        i +=1

    if i == 3 :
        pltNormalImage()
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(blurred_image2, cv2.COLOR_BGR2RGB))
        plt.title('Imagem 2d Suavizada (Filtro Gaussiano)')
        plt.show()
        i += 1