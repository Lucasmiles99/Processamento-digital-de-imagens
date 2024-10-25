def ler_imagem_pgm(caminho):
    with open(caminho, 'rb') as f:
        tipo = f.readline().decode().strip()  
        f.readline() 
        largura, altura = [int(i) for i in f.readline().decode().strip().split()]
        profundidade = int(f.readline().decode().strip()) 
        
        pixels = list(f.read())
    
    return tipo, largura, altura, profundidade, pixels

def escrever_imagem_pgm(caminho, tipo, largura, altura, profundidade, pixels):
    with open(caminho, 'wb') as f:
        f.write(f"{tipo}\n".encode()) 
        f.write(f"{largura} {altura}\n".encode()) 
        f.write(f"{profundidade}\n".encode()) 
        
        f.write(bytearray(pixels))

def converter_8bits_para_5bits(pixels):
    return [int((pixel / 255) * 31) for pixel in pixels]

caminho_entrada = 'Entrada_EscalaCinza.pgm'

tipo, largura, altura, profundidade, pixels = ler_imagem_pgm(caminho_entrada)

pixels_5bits = converter_8bits_para_5bits(pixels)

caminho_saida = 'Imagem_Convertida_5Bits.pgm'

escrever_imagem_pgm(caminho_saida, tipo, largura, altura, 31, pixels_5bits)

print(f"A imagem convertida foi salva em: {caminho_saida}")