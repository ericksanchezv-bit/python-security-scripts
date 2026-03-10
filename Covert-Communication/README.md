# 🕵️‍♂️ Covert Communication

This Python script embeds a text file (`CodeBook.txt`) into an image (`monalisa.bmp`) using **LSB (Least Significant Bit) steganography**.  
The result is a new image (`monaLisa_Hidden.bmp`) containing the hidden message.

---

## ✨ Features

- Embed any text file into a 24-bit RGB BMP image  
- Preserves original image dimensions and format  
- Displays a summary of bits embedded and pixels modified  

---

## ⚙️ Requirements

- Python 3.x  
- Libraries: `Pillow`  

Install dependencies:

```bash
pip install Pillow
