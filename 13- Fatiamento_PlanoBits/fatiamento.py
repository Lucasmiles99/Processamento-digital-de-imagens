class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[0 for _ in range(width)] for _ in range(height)]
    
    def set_pixel(self, x, y, value):
        self.pixels[y][x] = max(0, min(255, value))
    
    def get_pixel(self, x, y):
        return self.pixels[y][x]

def create_sample_image(width, height):
    img = Image(width, height)
    for y in range(height):
        for x in range(width):
            value = (x + y) % 256
            img.set_pixel(x, y, value)
    return img

def get_bit_plane(image, bit_position):
    result = Image(image.width, image.height)
    mask = 1 << (bit_position - 1)
    
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            bit_value = 1 if (pixel & mask) else 0
            result.set_pixel(x, y, bit_value)
    
    return result

def get_weighted_bit_plane(image, bit_position):
    result = Image(image.width, image.height)
    mask = 1 << (bit_position - 1)
    weight = 1 << (bit_position - 1) 
    
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            bit_value = weight if (pixel & mask) else 0
            result.set_pixel(x, y, bit_value)
    
    return result

def get_most_significant_bits(image, num_bits=3):
    result = Image(image.width, image.height)
    
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            new_value = 0
            for bit in range(8, 8-num_bits, -1):
                mask = 1 << (bit - 1)
                if pixel & mask:
                    new_value += 1 << (bit - 1)
            result.set_pixel(x, y, new_value)
    
    return result

def print_image_ascii(image, chars=None):
    if chars is None:
        chars = '@%#*+=-:. '
    
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            if isinstance(pixel, bool) or pixel <= 1:
                print('#' if pixel else '.', end='')
            else:
                char_idx = int(pixel / 256 * len(chars))
                char_idx = max(0, min(len(chars)-1, char_idx))
                print(chars[char_idx], end='')
        print()

def main():
    image = create_sample_image(32, 16)
    
    print("Imagem Original:")
    print_image_ascii(image)
    print("\n")
    
    print("Planos de Bits (Binários):")
    for bit in range(1, 9):
        print(f"\nPlano de Bits {bit}:")
        bit_plane = get_bit_plane(image, bit)
        print_image_ascii(bit_plane)
    
    print("\nPlanos de Bits (Com Pesos Posicionais):")
    for bit in range(1, 9):
        print(f"\nPlano de Bits {bit} (Peso {1 << (bit-1)}):")
        weighted_plane = get_weighted_bit_plane(image, bit)
        print_image_ascii(weighted_plane)
    
    print("\nImagem com 3 Bits Mais Significativos:")
    msb_image = get_most_significant_bits(image, 3)
    print_image_ascii(msb_image)

if __name__ == "__main__":
    main()