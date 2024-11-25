import csv
from collections import Counter
import os

# Função para ler a imagem em escala de cinza
def ler_imagem_pgm(caminho):
    if not os.path.exists(caminho):
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        return None

    with open(caminho, 'rb') as f:
        tipo = f.readline().decode().strip()
        linha = f.readline().decode().strip()
        
        # Ignora linhas de comentário
        while linha.startswith('#'):
            linha = f.readline().decode().strip()
        
        largura, altura = [int(i) for i in linha.split()]
        profundidade = int(f.readline().decode().strip())
        pixels = list(f.read())
    
    return largura, altura, profundidade, pixels

# Função para gerar o histograma e salvar em CSV
def gerar_histograma_escala_cinza(caminho_imagem, caminho_csv):
    resultado = ler_imagem_pgm(caminho_imagem)
    if resultado is None:
        print("Erro ao ler a imagem.")
        return
    
    largura, altura, profundidade, pixels = resultado
    frequencias = Counter(pixels)

    # Salva o histograma em formato CSV com colunas de Intensidade e Frequência
    with open(caminho_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Intensidade", "Frequência"])
        
        # Itera pelas intensidades de 0 a 255 para garantir todas as intensidades no CSV
        for intensidade in range(256):  # Valores de 0 a 255
            writer.writerow([intensidade, frequencias.get(intensidade, 0)])

# Caminhos de entrada e saída
base_dir = r'C:/Users/lucas/OneDrive/Área de Trabalho/IFC/PDI/9- Histograma de imagens/EscalaCinza.pgm'
caminho_imagem = os.path.join(base_dir, 'EntradaEscalaCinza.pgm')
caminho_csv = 'Histograma_EscalaCinza.csv'

# Imprime o caminho da imagem para verificar se está correto
print(f"Caminho da imagem: {caminho_imagem}")

# Gerar o CSV do histograma
gerar_histograma_escala_cinza(caminho_imagem, caminho_csv)
print(f"Arquivo CSV '{caminho_csv}' gerado com sucesso.")