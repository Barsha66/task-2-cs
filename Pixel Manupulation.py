from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path):
    try:
        img = Image.open(input_image_path)
        img_array = np.array(img)

        # Encrypt the image by adding 50 to each pixel value
        encrypted_array = (img_array + 50) % 128

        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_image.save(output_image_path)
        print(f"Image encrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_image_path, output_image_path):
    try:
        encrypted_img = Image.open(input_image_path)
        encrypted_array = np.array(encrypted_img)

        # Decrypt the image by subtracting 50 from each pixel value
        decrypted_array = (encrypted_array - 50) % 128

        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_image.save(output_image_path)
        print(f"Image decrypted and saved as {output_image_path}")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    # Specify the paths for the input and output images
    input_image_path = 'C:/Users/barsh/book.jpg'  # Change to your image path
    encrypted_image = 'C:/Users/barsh/encrypt/encrypted_image.jpg'  # Output for encrypted image
    decrypted_image = 'C:/Users/barsh/decrypt/decrypted_image.jpg'  # Output for decrypted image

    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image)

if __name__ == "__main__":
    main()

