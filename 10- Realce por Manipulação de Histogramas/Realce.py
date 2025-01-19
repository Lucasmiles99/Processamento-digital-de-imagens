def criar_arquivo_pgm(caminho):
    with open(caminho, 'w') as f:
        f.write("P2\n")  
        f.write("# Exemplo de arquivo PGM\n")  
        f.write("4 4\n")  
        f.write("255\n")  
        f.write("10 20 30 40\n")  
        f.write("50 60 70 80\n")  
        f.write("90 100 110 120\n")  
        f.write("130 140 150 160\n")  
    print(f"Arquivo '{caminho}' criado com sucesso.")

def ler_imagem_pgm(caminho):
    with open(caminho, 'r') as f:
        tipo = f.readline().strip()
        if tipo != "P2":
            raise ValueError("Arquivo PGM inválido. Apenas o formato P2 é suportado.")
        
        linha = f.readline().strip()
        while linha.startswith('#'):
            linha = f.readline().strip()
        
        try:
            largura, altura = map(int, linha.split())
        except ValueError:
            raise ValueError("Erro ao ler as dimensões da imagem (largura e altura). Verifique o arquivo PGM.")

        profundidade = int(f.readline().strip())
        if profundidade != 255:
            raise ValueError("A profundidade da imagem deve ser 255.")

        pixels = []
        for linha in f:
            if linha.strip():  
                pixels.extend(map(int, linha.split()))
        
        if len(pixels) != largura * altura:
            raise ValueError("O número de pixels não corresponde às dimensões especificadas no arquivo.")

        return pixels, largura, altura, profundidade

def aplicar_funcao_transferencia(pixels, largura, altura):
    max_val = max(pixels)
    min_val = min(pixels)
    pixels_transformados = [
        int((pixel - min_val) / (max_val - min_val) * 255) for pixel in pixels
    ]
    return pixels_transformados

def salvar_imagem_pgm(caminho, largura, altura, profundidade, pixels):
    with open(caminho, 'w') as f:
        f.write("P2\n")
        f.write(f"{largura} {altura}\n")
        f.write(f"{profundidade}\n")
        for i in range(altura):
            linha = pixels[i * largura:(i + 1) * largura]
            f.write(" ".join(map(str, linha)) + "\n")
    print(f"Imagem salva como '{caminho}'.")

def gerar_histograma(pixels):
    histograma = [0] * 256
    for pixel in pixels:
        histograma[pixel] += 1
    return histograma

def salvar_histograma_csv(caminho, histograma):
    with open(caminho, 'w') as f:
        f.write("Intensidade,Frequencia\n")
        for intensidade, frequencia in enumerate(histograma):
            f.write(f"{intensidade},{frequencia}\n")
    print(f"Histograma salvo como '{caminho}'.")

caminho_entrada = 'EntradaEscalaCinza.pgm'
caminho_saida = 'SaidaEscalaCinza.pgm'
caminho_histograma = 'Histograma.csv'

criar_arquivo_pgm(caminho_entrada)

pixels, largura, altura, profundidade = ler_imagem_pgm(caminho_entrada)

pixels_transformados = aplicar_funcao_transferencia(pixels, largura, altura)

salvar_imagem_pgm(caminho_saida, largura, altura, profundidade, pixels_transformados)

histograma = gerar_histograma(pixels_transformados)
salvar_histograma_csv(caminho_histograma, histograma)