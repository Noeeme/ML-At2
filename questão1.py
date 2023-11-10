import cv2
from matplotlib import pyplot as plt

image_path = "C:/Users/Noeeme/OneDrive/Imagens/image1.jpg"

image = cv2.imread(image_path)
if(image is not None) :
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title('Imagem 2d Colorida')
    plt.axis('off')
    plt.show()

height, width, channels = image.shape
dtype = image.dtype
print(f"Altura = {height}\n Largura = {width}\n Canais de cor = {channels}\n Tipo de dado = {dtype}\n")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
normalized_image = gray_image/255.0

print("Tom de cinza máximo = ", normalized_image.max())
print("Tom de cinza médio = ", normalized_image.mean())
print("Tom de cinza mínimo = ", normalized_image.min())

plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Imagem 2d Cinza')
plt.axis('off')
plt.show()