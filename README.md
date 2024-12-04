<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto de Detecção de Objetos com YOLOv5</title>
</head>
<body>

    <h1>Projeto de Detecção de Objetos com YOLOv5</h1>

    <p><strong>Descrição:</strong> Este projeto implementa a detecção de objetos utilizando o modelo YOLOv5. Ele é capaz de detectar uma grande variedade de objetos, como carros, pessoas e diversas categorias personalizadas. O objetivo deste projeto é demonstrar o uso do YOLOv5 para detecção de objetos em tempo real em imagens e vídeos.</p>

    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li>Python</li>
        <li>YOLOv5 (You Only Look Once v5)</li>
        <li>OpenCV</li>
        <li>Pillow</li>
        <li>PyTorch</li>
    </ul>

    <h2>Configuração do Projeto</h2>
    <ol>
        <li>Clone este repositório para sua máquina local:</li>
        <pre><code>git clone https://github.com/seuusuario/yolov5-deteccao-objetos.git</code></pre>

        <li>Vá para o diretório do projeto:</li>
        <pre><code>cd yolov5-deteccao-objetos</code></pre>

        <li>Crie um ambiente virtual e ative-o (opcional, mas recomendado):</li>
        <pre><code>python3 -m venv venv</code></pre>
        <pre><code>source venv/bin/activate</code></pre>

        <li>Instale as dependências:</li>
        <pre><code>pip install -r requirements.txt</code></pre>

        <li>Baixe os pesos pré-treinados do YOLOv5:</li>
        <pre><code>wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt</code></pre>
    </ol>

    <h2>Como Rodar o Código</h2>
    <ol>
        <li>Prepare a imagem ou vídeo de entrada. Certifique-se de que está no diretório correto.</li>
        <li>Execute o seguinte comando para realizar a detecção de objetos:</li>
        <pre><code>python detect.py --source caminho_da_sua_imagem_ou_video</code></pre>
        <li>Veja os resultados da detecção no diretório de saída.</li>
    </ol>

    <h2>Notas Importantes</h2>
    <ul>
        <li>Certifique-se de estar usando a versão correta do Python e as dependências conforme indicado na configuração do projeto.</li>
        <li>As imagens de entrada devem estar em um formato compatível (por exemplo, .jpg, .png).</li>
        <li>Se desejar adicionar novas classes ou treinar o modelo novamente, siga as orientações de treinamento do YOLOv5.</li>
    </ul>

    <h2>Contribuindo</h2>
    <p>Se você deseja contribuir para este projeto, fique à vontade para fazer um fork, realizar as modificações e enviar um pull request. Certifique-se de que seu código siga o estilo de codificação do projeto.</p>

    <h2>Créditos</h2>
    <ul>
        <li>YOLOv5: https://github.com/ultralytics/yolov5</li>
        <li>Autores originais do algoritmo YOLOv5: Ultralytics</li>
        <li>OpenCV: https://opencv.org/</li>
        <li>PyTorch: https://pytorch.org/</li>
    </ul>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a Licença MIT - veja o arquivo <a href="LICENSE">LICENSE</a> para mais detalhes.</p>

</body>
</html>
