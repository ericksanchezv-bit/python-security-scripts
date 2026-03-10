"""
🕵️‍♂️ Covert Communication (LSB Embedder)

This script embeds the contents of a text file (`CodeBook.txt`) into a 24-bit RGB image (`monalisa.bmp`) 
using **Least Significant Bit (LSB) steganography**.

- Reads the file as bytes and converts to bits
- Embeds bits into the RGB channels of each pixel
- Produces a new image (`monaLisa_Hidden.bmp`) with the hidden message

"""

from PIL import Image
import os
import sys

def file_to_bits(path):
    
    with open(path, 'rb') as f:
        data = f.read()
    data += b'\x00'  
    bits = ''.join(f'{byte:08b}' for byte in data)
    return bits, len(data)

def set_lsb(value, bit):
    
    return (value & 0b11111110) | int(bit)

def embed_bits_into_image(img_path, out_path, bits):
    
    img = Image.open(img_path)
    if img.mode != 'RGB':
        raise ValueError("Input image must be 24-bit RGB (True Color BMP).")

    pix = img.load()
    width, height = img.size
    capacity = width * height * 3

    if len(bits) > capacity:
        raise ValueError(f"Message too large for image ({len(bits)} bits > {capacity} bits).")

    bit_index = 0
    for y in range(height):
        for x in range(width):
            if bit_index >= len(bits):
                break

            r, g, b = pix[x, y]
            if bit_index < len(bits):
                r = set_lsb(r, bits[bit_index])
                bit_index += 1
            if bit_index < len(bits):
                g = set_lsb(g, bits[bit_index])
                bit_index += 1
            if bit_index < len(bits):
                b = set_lsb(b, bits[bit_index])
                bit_index += 1

            pix[x, y] = (r, g, b)

        if bit_index >= len(bits):
            break

    img.save(out_path)
    return bit_index, width, height

def main():
    img_path = "monalisa.bmp"
    codebook_path = "CodeBook.txt"
    out_path = "monaLisa_Hidden.bmp"

    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        sys.exit(1)
    if not os.path.exists(codebook_path):
        print(f"CodeBook not found: {codebook_path}")
        sys.exit(1)

    print("=== Full CodeBook LSB Embedder ===")
    print(f"Embedding contents of: {codebook_path}")
    print(f"Into image: {img_path}")

    try:
        bits, total_bytes = file_to_bits(codebook_path)
        print(f"Read {total_bytes} bytes from CodeBook.txt (includes terminator).")

        embedded_bits, w, h = embed_bits_into_image(img_path, out_path, bits)
        print("\nEmbedding Complete!")
        print(f"Bits embedded: {embedded_bits}")
        print(f"Pixels modified: {embedded_bits // 3}")
        print(f"Image size: {w}x{h}  |  Mode: RGB")
        print(f"Output file created: {out_path}")
        print("\n(Same format and dimensions as original.)")

    except Exception as e:
        print("Embedding failed:", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
