def ler_pgm(caminho):
    """Lê um arquivo PGM (grayscale) e retorna o cabeçalho e os pixels."""
    with open(caminho, "r") as f:
        linhas = f.readlines()

    assert linhas[0].strip() == "P2", "Formato inválido! O código só suporta PGM P2."
    
    largura, altura = map(int, linhas[1].strip().split())
    max_val = int(linhas[2].strip())
    
    pixels = [int(valor) for linha in linhas[3:] for valor in linha.split()]
    
    return largura, altura, max_val, pixels

def salvar_pgm(caminho, largura, altura, max_val, pixels):
    """Salva uma imagem PGM P2 processada."""
    with open(caminho, "w") as f:
        f.write(f"P2\n{largura} {altura}\n{max_val}\n")
        for i, valor in enumerate(pixels):
            f.write(f"{valor} ")
            if (i + 1) % largura == 0:
                f.write("\n")

def funcao_transferencia(pixels, max_val):
    """Aplica uma função de transferência para melhorar o contraste."""
    minimo = min(pixels)
    maximo = max(pixels)
    
    # Normalização simples
    return [int((p - minimo) / (maximo - minimo) * max_val) for p in pixels]

def gerar_histograma(pixels, max_val):
    """Gera um histograma textual no terminal."""
    histograma = [0] * (max_val + 1)
    for p in pixels:
        histograma[p] += 1

    print("\n=== HISTOGRAMA ===")
    for i, freq in enumerate(histograma):
        if freq > 0:
            print(f"{i:3}: {'#' * (freq // 100)}")  # Escala de 100 pixels

def processar_pgm(arquivo_entrada, arquivo_saida):
    """Processa uma imagem PGM aplicando a função de transferência e gerando histograma."""
    largura, altura, max_val, pixels = ler_pgm(arquivo_entrada)
    novos_pixels = funcao_transferencia(pixels, max_val)
    
    gerar_histograma(novos_pixels, max_val)
    salvar_pgm(arquivo_saida, largura, altura, max_val, novos_pixels)
    print(f"Imagem processada salva em: {arquivo_saida}")

# ============================
#        PROCESSAR PPM
# ============================

def ler_ppm(caminho):
    """Lê um arquivo PPM (RGB) e retorna cabeçalho e os pixels."""
    with open(caminho, "r") as f:
        linhas = f.readlines()

    assert linhas[0].strip() == "P3", "Formato inválido! O código só suporta PPM P3."
    
    largura, altura = map(int, linhas[1].strip().split())
    max_val = int(linhas[2].strip())
    
    pixels = [int(valor) for linha in linhas[3:] for valor in linha.split()]
    
    return largura, altura, max_val, pixels

def salvar_ppm(caminho, largura, altura, max_val, pixels):
    """Salva uma imagem PPM P3 processada."""
    with open(caminho, "w") as f:
        f.write(f"P3\n{largura} {altura}\n{max_val}\n")
        for i, valor in enumerate(pixels):
            f.write(f"{valor} ")
            if (i + 1) % (largura * 3) == 0:
                f.write("\n")

def processar_ppm(arquivo_entrada, arquivo_saida):
    """Processa uma imagem PPM aplicando a função de transferência e gerando histogramas para R, G e B."""
    largura, altura, max_val, pixels = ler_ppm(arquivo_entrada)

    canais = [pixels[i::3] for i in range(3)]  # Separar canais R, G, B
    
    novos_canais = [funcao_transferencia(canal, max_val) for canal in canais]

    print("\n=== HISTOGRAMA CANAL VERMELHO (R) ===")
    gerar_histograma(novos_canais[0], max_val)
    print("\n=== HISTOGRAMA CANAL VERDE (G) ===")
    gerar_histograma(novos_canais[1], max_val)
    print("\n=== HISTOGRAMA CANAL AZUL (B) ===")
    gerar_histograma(novos_canais[2], max_val)

    novos_pixels = [valor for tripla in zip(*novos_canais) for valor in tripla]
    
    salvar_ppm(arquivo_saida, largura, altura, max_val, novos_pixels)
    print(f"Imagem processada salva em: {arquivo_saida}")

# ============================
#        EXECUÇÃO
# ============================
if __name__ == "__main__":
    print("Escolha o tipo de imagem para processar:")
    print("1 - PGM (escala de cinza)")
    print("2 - PPM (RGB)")
    opcao = input("Digite sua escolha (1 ou 2): ")

    if opcao == "1":
        entrada = input("Digite o caminho do arquivo PGM de entrada: ")
        saida = input("Digite o caminho do arquivo PGM de saída: ")
        processar_pgm(entrada, saida)
    
    elif opcao == "2":
        entrada = input("Digite o caminho do arquivo PPM de entrada: ")
        saida = input("Digite o caminho do arquivo PPM de saída: ")
        processar_ppm(entrada, saida)

    else:
        print("Opção inválida!")