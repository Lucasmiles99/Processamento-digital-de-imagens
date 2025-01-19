def read_ppm(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
    
    assert lines[0] == 'P3', "Formato de arquivo inválido!"
    
    width, height = map(int, lines[1].split())
    max_val = int(lines[2])
    
    pixels = list(map(int, " ".join(lines[3:]).split()))
    
    return width, height, max_val, pixels


def write_ppm(filename, width, height, max_val, pixels):
    with open(filename, 'w') as f:
        f.write(f"P3\n{width} {height}\n{max_val}\n")
        for i in range(0, len(pixels), 3):
            f.write(f"{pixels[i]} {pixels[i+1]} {pixels[i+2]} ")
            if (i // 3 + 1) % width == 0:
                f.write("\n")


def separate_colors_min(width, height, max_val, pixels):
    red = []
    green = []
    blue = []
    
    for i in range(0, len(pixels), 3):
        r, g, b = pixels[i], pixels[i+1], pixels[i+2]
        
        red.extend([r, 0, 0])
        green.extend([0, g, 0])
        blue.extend([0, 0, b])
    
    write_ppm("Fig4_red_min.ppm", width, height, max_val, red)
    write_ppm("Fig4_green_min.ppm", width, height, max_val, green)
    write_ppm("Fig4_blue_min.ppm", width, height, max_val, blue)


def separate_colors_max(width, height, max_val, pixels):
    red = []
    green = []
    blue = []
    
    for i in range(0, len(pixels), 3):
        r, g, b = pixels[i], pixels[i+1], pixels[i+2]
        
        red.extend([r, max_val, max_val])
        green.extend([max_val, g, max_val])
        blue.extend([max_val, max_val, b])
    
    write_ppm("Fig4_red_max.ppm", width, height, max_val, red)
    write_ppm("Fig4_green_max.ppm", width, height, max_val, green)
    write_ppm("Fig4_blue_max.ppm", width, height, max_val, blue)

input_file = "Fig4.ppm"
width, height, max_val, pixels = read_ppm(input_file)

separate_colors_min(width, height, max_val, pixels)

separate_colors_max(width, height, max_val, pixels)

print("Imagens geradas: Fig4_red_min.ppm, Fig4_green_min.ppm, Fig4_blue_min.ppm, Fig4_red_max.ppm, Fig4_green_max.ppm, Fig4_blue_max.ppm")