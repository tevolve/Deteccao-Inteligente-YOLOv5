# Instalar dependências
!pip install torch torchvision torchaudio
!pip install yolov5

# Importar bibliotecas necessárias
import torch
import requests
from PIL import Image
import matplotlib.pyplot as plt

# Baixar uma imagem de teste do COCO
image_url = 'https://raw.githubusercontent.com/ultralytics/yolov5/master/data/images/bus.jpg'  # URL de uma imagem pública
response = requests.get(image_url)  # Fazendo o download da imagem

# Abrir a imagem usando PIL
image = Image.open(BytesIO(response.content))

# Exibir a imagem
plt.imshow(image)
plt.axis('off')  # Desligar os eixos
plt.show()

# Carregar o modelo YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' é o modelo mais rápido e leve

# Salvar a imagem localmente (necessário para YOLOv5 processar)
image_path = "/content/test_image.jpg"
image.save(image_path)

# Realizar a detecção com YOLOv5
results = model(image_path)

# Exibir resultados da detecção
results.show()  # Exibir as caixas delimitadoras e as classes detectadas

# Salvar a imagem com as detecções
results.save()  # Salva a imagem com as detecções realizadas

# Exibir as classes detectadas
detected_classes = results.names  # Detalhes sobre as classes detectadas
print("Classes detectadas:", detected_classes)

# Exibir as boxes e classes detectadas na imagem
for *box, conf, cls in results.xywh[0]:
    print(f"Classe: {detected_classes[int(cls)]} com confiança {conf:.2f} e caixa: {box}")
