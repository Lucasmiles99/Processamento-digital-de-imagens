def carregar_pgm(caminho):
    with open(caminho, 'r') as arquivo:
        tipo = arquivo.readline().strip()
        if tipo != 'P2':
            raise ValueError("O arquivo não está no formato P2 (PGM em escala de cinza).")
        
        while True:
            linha = arquivo.readline().strip()
            if linha.startswith('#'):
                continue
            else:
                largura, altura = map(int, linha.split())
                break
        
        max_valor = int(arquivo.readline().strip())
        
        pixels = []
        for linha in arquivo:
            pixels.extend(map(int, linha.split()))
    
    return largura, altura, max_valor, pixels

def salvar_pgm(caminho, largura, altura, max_valor, pixels):
    with open(caminho, 'w') as arquivo:
        arquivo.write('P2\n')
        arquivo.write(f'{largura} {altura}\n')
        arquivo.write(f'{max_valor}\n')
        for i, pixel in enumerate(pixels):
            arquivo.write(f'{pixel} ')
            if (i + 1) % largura == 0:
                arquivo.write('\n')

def converter_para_5_bits(pixels):
    nova_imagem = [pixel // 8 for pixel in pixels]  
    return nova_imagem

caminho_original = 'Entrada_EscalaCinza.pgm'  
caminho_convertido_5_bits = 'Saida_5Bits.pgm'

largura, altura, max_valor, pixels = carregar_pgm(caminho_original)
pixels_5_bits = converter_para_5_bits(pixels)
salvar_pgm(caminho_convertido_5_bits, largura, altura, 31, pixels_5_bits)

print("Imagem convertida e salva com sucesso!")