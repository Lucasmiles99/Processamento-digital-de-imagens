import csv
from collections import Counter
import os

def salvar_como_ppm(caminho, largura, altura, pixels):
    with open(caminho, 'wb') as f:
        f.write(b'P6\n')  
        f.write(f"{largura} {altura}\n".encode()) 
        f.write(b'255\n')  
        
        for y in range(altura):
            for x in range(largura):
                r, g, b = pixels[y][x]
                f.write(bytes([r, g, b]))

def ler_imagem_ppm(caminho):
    if not os.path.exists(caminho):
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        return None

    with open(caminho, 'rb') as f:
        tipo = f.readline().decode().strip()

        if tipo != 'P6':
            print("Erro: A imagem não está no formato PPM (P6).")
            return None, None, None

        linha = f.readline().decode().strip()
        while linha.startswith('#'):
            linha = f.readline().decode().strip()

        largura, altura = [int(i) for i in linha.split()]

        profundidade = int(f.readline().decode().strip())
        if profundidade != 255:
            print("Erro: A profundidade da imagem não é 255.")
            return None, None, None

        dados = list(f.read())

    return largura, altura, dados

def gerar_histogramas_rgb(caminho_imagem, caminho_csv):
    largura, altura, dados = ler_imagem_ppm(caminho_imagem)
    if dados is None:
        print("Erro ao ler a imagem.")
        return

    canal_r = dados[0::3]  
    canal_g = dados[1::3]  
    canal_b = dados[2::3]  

    frequencias_r = Counter(canal_r)
    frequencias_g = Counter(canal_g)
    frequencias_b = Counter(canal_b)

    with open(caminho_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Intensidade", "Frequência_R", "Frequência_G", "Frequência_B"])

        for intensidade in range(256): 
            writer.writerow([
                intensidade,
                frequencias_r.get(intensidade, 0),
                frequencias_g.get(intensidade, 0),
                frequencias_b.get(intensidade, 0)
            ])

    print(f"Arquivo CSV '{caminho_csv}' gerado com sucesso.")

largura = 3
altura = 2

pixels = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)], 
    [(255, 255, 0), (0, 255, 255), (255, 0, 255)]  
]

caminho_imagem = 'EntradaRGB.ppm'
caminho_csv = 'Histograma_RGB.csv'

salvar_como_ppm(caminho_imagem, largura, altura, pixels)
print(f"Imagem salva como '{caminho_imagem}'.")

gerar_histogramas_rgb(caminho_imagem, caminho_csv)
print(f"Arquivo CSV '{caminho_csv}' gerado com sucesso.")