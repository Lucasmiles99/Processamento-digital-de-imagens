def save_ppm(filename, width, height, pixels):
    with open(filename, 'w') as f:
        
        f.write("P3\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")
        
        for row in pixels:
            for pixel in row:
                f.write(f"{pixel[0]} {pixel[1]} {pixel[2]} ")
            f.write("\n")

width_homo, height_homo = 10, 10
pixels_homo = [[[200, 200, 200] for _ in range(width_homo)] for _ in range(height_homo)]

width_non_homo, height_non_homo = 10, 10
pixels_non_homo = [[[i * 25 % 256, j * 25 % 256, (i + j) * 15 % 256] 
                    for i in range(width_non_homo)] for j in range(height_non_homo)]

save_ppm("imagem_homogenea.ppm", width_homo, height_homo, pixels_homo)
save_ppm("imagem_nao_homogenea.ppm", width_non_homo, height_non_homo, pixels_non_homo)

"/imagem_homogenea.ppm", "/imagem_nao_homogenea.ppm"