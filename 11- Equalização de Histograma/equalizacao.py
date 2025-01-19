import numpy as np
from PIL import Image
import os

def equalize_histogram(image_array):
    hist = np.zeros(256, dtype=int)
    for pixel in image_array.flatten():
        hist[pixel] += 1

    cdf = np.cumsum(hist)
    cdf_min = cdf[np.nonzero(cdf)].min()
    total_pixels = image_array.size
    cdf_normalized = (cdf - cdf_min) / (total_pixels - cdf_min) * 255
    cdf_normalized = cdf_normalized.astype('uint8')

    equalized_image = cdf_normalized[image_array]
    return equalized_image

image_files = [
    "Fig0316(1)(top_left).tif",
    "Fig0316(2)(2nd_from_top).tif",
    "Fig0316(3)(third_from_top).tif",
    "Fig0316(4)(bottom_left).tif",
]

for image_file in image_files:
    try:
        image = Image.open(image_file).convert("L")  
        image_array = np.array(image)

        equalized_array = equalize_histogram(image_array)

        equalized_image = Image.fromarray(equalized_array)
        output_name = f"equalized_{image_file}"
        equalized_image.save(output_name)

        print(f"Imagem {image_file} processada e salva como {output_name}.")
    except FileNotFoundError:
        print(f"Arquivo {image_file} não encontrado. Certifique-se de que está no mesmo diretório do script.")
    except Exception as e:
        print(f"Erro ao processar {image_file}: {e}")