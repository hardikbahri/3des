# Triple DES Image Encryptor-Decryptor

This project is a command-line tool for encrypting and decrypting images using Triple DES (Data Encryption Standard) encryption. It ensures the security of your images by encrypting them with a user-provided password and a salt value. The encrypted images can only be decrypted using the correct password.

## Features

- **Triple DES Encryption:** Uses Triple DES encryption for added security.
- **SHA256 Hashing:** Utilizes SHA256 hashing to verify the integrity of the original and decrypted images.
- **Password Protection:** Requires a minimum 8-character password for encryption and decryption.
- **Salting:** Adds a salt to the password before hashing to enhance security.

## Prerequisites

- Python 3.x
- Required Python libraries: `pycryptodome`

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/triple-des-encryptor-decryptor.git
   cd triple-des-encryptor-decryptor
   ```

2. **Install the required libraries:**
   ```sh
   pip install pycryptodome
   ```

## Usage

1. **Run the program:**
   ```sh
   python encryptor_decryptor.py
   ```

2. **Choose the mode:**
   - Press `1` for Encryption
   - Press `2` for Decryption

### Encryption

- **Enter the file name to be encrypted:** Provide the name of the image file you want to encrypt. Ensure the file is in the same directory as the script.
- **Enter a password:** The password must be at least 8 characters long. Re-enter the password for confirmation.
- **Encryption Process:** The image will be encrypted using Triple DES and saved with a new name prefixed with "encrypted_".
  
  Example:
  ```
  Enter file's name to be encypted: image.jpg
  Enter minimum 8 character long password: ********
  Enter password again: ********
  ```

### Decryption

- **Enter the encrypted file name:** Provide the name of the encrypted image file. Ensure the file is in the same directory as the script.
- **Enter the password:** Enter the password used for encryption.
- **Decryption Process:** The image will be decrypted and saved with a new name prefixed with "decrypted_".
  
  Example:
  ```
  Enter file's name to decrypted: encrypted_image.jpg
  Enter password: ********
  ```

## Code Overview

### `encryptor(path)`

- Reads the image file in binary mode.
- Pads the image data to ensure its length is a multiple of 8.
- Prompts the user for a password and confirms it.
- Uses PBKDF2 to hash and salt the password.
- Encrypts the image data using Triple DES.
- Appends a SHA256 hash of the original image to the encrypted data.
- Saves the encrypted data to a new file.

### `decryptor(encrypted_image_path)`

- Reads the encrypted image file in binary mode.
- Prompts the user for the decryption password.
- Extracts the SHA256 hash from the encrypted data.
- Uses PBKDF2 to hash and salt the password.
- Decrypts the image data using Triple DES.
- Compares the hash of the decrypted data with the extracted hash.
- Saves the decrypted data to a new file if the hashes match.

