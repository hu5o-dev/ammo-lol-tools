# 📄 Ammo lol tools README

Welcome to this project! Below, you'll find descriptions and usage instructions for three different Python scripts included in this repository. Each script has a specific purpose and can be used for various tasks, such as generating API keys, upscaling images, and fetching user data from an API.

---

## 🔑 API Key Generation and Testing

This script generates random API keys and tests them against a specific endpoint to check their validity.

### 📋 Code Overview

- **`generate_api_key(length=40)`**: Generates a random API key with a default length of 40 characters.
- **`test_api_key(api_key)`**: Tests the generated API key by making a GET request to the specified URL. If the key is valid, it saves the user information in a JSON file.
- **Loop**: Continuously generates and tests API keys until a valid one is found.

### 🚀 Usage

To run the script, simply execute it in your Python environment. The script will automatically generate and test API keys:

```python
python api_key_generator.py
```

This script will stop once a valid API key is found and save the corresponding user information to a file.

---

## 🖼️ Image Upscaling Script

This script upscales an image by a specified factor and saves the output to a new file.

### 📋 Code Overview

- **`upscale_image(input_path, output_path, scale_factor)`**: Upscales the image at `input_path` by `scale_factor` and saves it to `output_path`.

### 🚀 Usage

To upscale an image, run the script with the following command:

```bash
python upscale_image.py <input_image> <output_image> <scale_factor>
```

For example:

```bash
python upscale_image.py input.jpg output.jpg 2.0
```

This command will double the size of `input.jpg` and save it as `output.jpg`.

---

## 👤 User Data Retrieval Script

This script fetches user data from a public API and saves it to a file.

### 📋 Code Overview

- **API URL**: `https://ammo.lol/api/v1/public/user`
- **Headers**: Includes the required API key.
- **API KEY**: Temeber before running script change the api section to your key.
- **Loop**: Continuously fetches user data for incrementing `uid` values until it encounters an error.

### 🚀 Usage

To run the script, simply execute it:

```python
python fetch_user_data.py
```

The script will save user information to files in the `users` directory, with each file named according to the user's UID.

---

Enjoy using the scripts! If you have any questions or issues, feel free to reach out. 😊
