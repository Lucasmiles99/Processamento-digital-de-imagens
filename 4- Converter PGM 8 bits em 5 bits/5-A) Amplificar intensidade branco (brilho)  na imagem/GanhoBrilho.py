def aplicar_ganho_brilho(pixels, max_valor):
    nova_imagem = [min(int(pixel * 1.2), max_valor) for pixel in pixels] 
    return nova_imagem

caminho_ganho_brilho = 'Saida_GanhoBrilho_5Bits.pgm'

pixels_com_ganho = aplicar_ganho_brilho(pixels_5_bits, 31)
salvar_pgm(caminho_ganho_brilho, largura, altura, 31, pixels_com_ganho)

caminho_ganho_brilho