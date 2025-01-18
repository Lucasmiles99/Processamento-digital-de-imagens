def read_ppm(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
    
    # Ler o cabeçalho
    assert lines[0] == 'P3', "Formato de arquivo inválido!"
    
    width, height = map(int, lines[1].split())
    max_val = int(lines[2])
    
    # Ler os pixels
    pixels = list(map(int, " ".join(lines[3:]).split()))
    
    return width, height, max_val, pixels


def write_pgm(filename, width, height, max_val, pixels):
    with open(filename, 'w') as f:
        f.write(f"P2\n{width} {height}\n{max_val}\n")
        for i in range(0, len(pixels), 3):
            gray = sum(pixels[i:i+3]) // 3  # Média dos valores RGB
            f.write(f"{gray} ")
            if (i // 3 + 1) % width == 0:
                f.write("\n")


def write_ppm(filename, width, height, max_val, pixels):
    with open(filename, 'w') as f:
        f.write(f"P3\n{width} {height}\n{max_val}\n")
        for i in range(0, len(pixels), 3):
            avg = sum(pixels[i:i+3]) // 3  # Média dos valores RGB
            f.write(f"{avg} {avg} {avg} ")
            if (i // 3 + 1) % width == 0:
                f.write("\n")


# Ler a imagem original
input_file = "Fig4.ppm"
width, height, max_val, pixels = read_ppm(input_file)

# Gerar imagem em escala de cinza
write_pgm("Fig4_gray.pgm", width, height, max_val, pixels)

# Gerar imagem P3 com média dos valores RGB
write_ppm("Fig4_avg.ppm", width, height, max_val, pixels)

print("Imagens geradas: Fig4_gray.pgm (P2) e Fig4_avg.ppm (P3)")