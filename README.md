# Description
This project demonstrates a simple approach to image encryption and decryption using Python's PIL and NumPy libraries. The encryption process involves modifying pixel values by adding a fixed value, while decryption reverses this by subtracting the same value. This is a basic yet effective technique for visually transforming an image to obscure its original content.

# Features
Image Encryption: Encrypts an image by adjusting pixel values and saves the transformed output as a new file.
Image Decryption: Reverses the encryption by restoring the original pixel values, recreating the original image.
Customizable Paths: Users can easily specify paths for input and output images, allowing flexibility in image processing.
Error Handling: Includes error handling to manage potential issues in file processing or input/output operations.

# Usage
Prepare Input and Output Paths: Define the file paths for the input image, the encrypted image, and the decrypted output.
Run the Program: Execute the program to generate the encrypted image file, then decrypt it to restore the original image.
View Results: The output files for both encryption and decryption will be saved to the paths specified, allowing users to verify the results.

# Example
Suppose the input image is a JPEG file located at a specified path. Running the program will generate an encrypted version that appears altered due to pixel adjustments. After decryption, the output image file will resemble the original.
