from PIL import Image

def encrypt_image(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")  # Ensures RGBA mode
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b, a = pixels[i, j]  # Include alpha
            pixels[i, j] = (255 - r, 255 - g, 255 - b, a)  # Keep alpha unchanged

    img.save(output_path)
    print("Image encrypted and saved as:", output_path)

def decrypt_image(input_path, output_path):
    encrypt_image(input_path, output_path)

encrypt_image("original.png", "encrypted.png")
decrypt_image("encrypted.png", "decrypted.png")
