# Função para carregar a imagem PGM
def carregar_pgm(caminho):
    with open(caminho, 'r') as arquivo:
        # Ler o cabeçalho
        tipo = arquivo.readline().strip()
        if tipo != 'P2':
            raise ValueError("O arquivo não está no formato P2 (PGM em escala de cinza).")
        
        # Ignorar comentários
        while True:
            linha = arquivo.readline().strip()
            if linha.startswith('#'):
                continue
            else:
                largura, altura = map(int, linha.split())
                break
        
        # Ler o valor máximo de cinza
        max_valor = int(arquivo.readline().strip())
        
        # Ler os pixels
        pixels = []
        for linha in arquivo:
            pixels.extend(map(int, linha.split()))
    
    return largura, altura, max_valor, pixels

# Função para salvar a imagem PGM
def salvar_pgm(caminho, largura, altura, max_valor, pixels):
    with open(caminho, 'w') as arquivo:
        arquivo.write('P2\n')
        arquivo.write(f'{largura} {altura}\n')
        arquivo.write(f'{max_valor}\n')
        for i, pixel in enumerate(pixels):
            arquivo.write(f'{pixel} ')
            if (i + 1) % largura == 0:
                arquivo.write('\n')

# Função para converter os pixels de 8 bits para 5 bits
def converter_para_5_bits(pixels):
    nova_imagem = [pixel // 8 for pixel in pixels]  # Dividir cada pixel por 8 e truncar
    return nova_imagem

# Caminho do arquivo original e do arquivo de saída
caminho_original = 'Entrada_EscalaCinza.pgm'  # Ajuste o caminho se necessário
caminho_convertido_5_bits = 'Saida_5Bits.pgm'

# Executar as funções
largura, altura, max_valor, pixels = carregar_pgm(caminho_original)
pixels_5_bits = converter_para_5_bits(pixels)
salvar_pgm(caminho_convertido_5_bits, largura, altura, 31, pixels_5_bits)

print("Imagem convertida e salva com sucesso!")