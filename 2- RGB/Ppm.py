import random

def gerar_ppm_100x100_completo():
    largura, altura = 100, 100
    max_valor = 15  
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
    
    with open("imagem_100x100_completa.ppm", "w") as f:
        f.write("\n".join(imagem))

gerar_ppm_100x100_completo()