import math

def ler_imagem_pgm(caminho):
    with open(caminho, 'r') as f:
        tipo = f.readline().strip()  
        if tipo != 'P2':
            raise ValueError("Formato PGM não suportado. Apenas 'P2' é aceito.")

        linha = f.readline().strip()
        while linha.startswith('#'):
            linha = f.readline().strip()

        largura, altura = map(int, linha.split())  
        profundidade = int(f.readline().strip())  

        pixels = []
        for y in range(altura):
            linha_pixels = list(map(int, f.readline().split()))
            pixels.append(linha_pixels)

    return pixels, largura, altura, profundidade

def salvar_imagem_pgm(caminho, pixels, largura, altura, profundidade):
    with open(caminho, 'w') as f:
        f.write("P2\n")
        f.write(f"{largura} {altura}\n")
        f.write(f"{profundidade}\n")
        for y in range(altura):
            f.write(' '.join(map(str, pixels[y])) + '\n')
    print(f"Imagem salva como: {caminho}")

def exibir_histograma(frequencias):
    max_freq = max(frequencias)  
    escala = 50  

    print("\nHistograma da Imagem:")
    for intensidade in range(256):
        barras = int((frequencias[intensidade] / max_freq) * escala) if max_freq > 0 else 0
        print(f"{intensidade:3}: {'█' * barras} ({frequencias[intensidade]})")

def salvar_histograma_csv(histograma, caminho_csv):
    with open(caminho_csv, 'w') as f:
        f.write("Intensidade,Frequencia\n")
        for intensidade, freq in enumerate(histograma):
            f.write(f"{intensidade},{freq}\n")
    print(f"Histograma salvo como: {caminho_csv}")

def aplicar_transferencia(pixels, largura, altura, profundidade, tipo="linear"):
    tabela = list(range(256))  

    if tipo == "logaritmica":
        tabela = [int(255 * (math.log(1 + i) / math.log(256))) for i in range(256)]
    elif tipo == "exponencial":
        tabela = [int((255 / (math.exp(1) - 1)) * (math.exp(i / 255) - 1)) for i in range(256)]

    pixels_transformados = [
        [tabela[pixels[y][x]] for x in range(largura)]
        for y in range(altura)
    ]

    return pixels_transformados

def calcular_histograma(pixels, largura, altura):
    histograma = [0] * 256
    for y in range(altura):
        for x in range(largura):
            intensidade = pixels[y][x]
            histograma[intensidade] += 1
    return histograma

def processar_imagem(caminho_entrada, caminho_saida, tipo_transferencia="linear"):
    pixels, largura, altura, profundidade = ler_imagem_pgm(caminho_entrada)

    histograma_original = calcular_histograma(pixels, largura, altura)
    exibir_histograma(histograma_original)
    salvar_histograma_csv(histograma_original, "HistogramaOriginal.csv")

    pixels_transformados = aplicar_transferencia(pixels, largura, altura, profundidade, tipo_transferencia)

    histograma_transformado = calcular_histograma(pixels_transformados, largura, altura)
    exibir_histograma(histograma_transformado)
    salvar_histograma_csv(histograma_transformado, "HistogramaTransformado.csv")

    salvar_imagem_pgm(caminho_saida, pixels_transformados, largura, altura, profundidade)

    print(f"Imagem transformada salva como: {caminho_saida}")

caminho_entrada = 'EntradaEscalaCinza.pgm'
caminho_saida = 'SaidaEscalaCinza.pgm'
processar_imagem(caminho_entrada, caminho_saida, tipo_transferencia="logaritmica")