import random

def gerar_ppm_1000x1000():
    largura, altura = 1000, 1000
    max_valor = 255 
    imagem = []
    
    imagem.append(f"P3\n{largura} {altura}\n{max_valor}")
    
    for _ in range(altura):
        linha = []
        for _ in range(largura):
            r = random.randint(0, max_valor)
            g = random.randint(0, max_valor)
            b = random.randint(0, max_valor)
            linha.append(f"{r} {g} {b}")
        imagem.append(" ".join(linha))
    
    with open("imagem_1000x1000.ppm", "w") as f:
        f.write("\n".join(imagem))

gerar_ppm_1000x1000()