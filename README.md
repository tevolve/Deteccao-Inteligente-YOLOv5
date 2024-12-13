# Detecção de Objetos com YOLOv5

Este projeto demonstra a utilização do modelo **YOLOv5** para detecção de objetos em imagens. O código realiza os seguintes passos:

1. **Baixa uma imagem de teste** de um link público.
2. **Carrega o modelo YOLOv5** pré-treinado.
3. **Realiza a detecção de objetos** na imagem utilizando o YOLOv5.
4. **Exibe a imagem original** com as caixas delimitadoras ao redor dos objetos detectados.
5. **Salva a imagem** com as detecções realizadas.
6. **Exibe as classes detectadas** e as caixas delimitadoras para cada objeto.

## Instalação

Para executar o projeto, instale as dependências necessárias:

```bash
!pip install torch torchvision torchaudio
!pip install yolov5
```
## Execução
Após instalar as dependências, basta executar o código para realizar a detecção de objetos na imagem de teste.

## Resultados Esperados
- O modelo YOLOv5 detectará objetos como pessoas, veículos, e outros itens presentes na imagem.
- As caixas delimitadoras serão desenhadas ao redor de cada objeto detectado.
- O modelo irá salvar a imagem com as detecções realizadas.

## Contribuições
Contribuições são bem-vindas. Para sugerir melhorias ou corrigir erros, envie um pull request.

## Licença
Este projeto é licenciado sob a Licença MIT.

