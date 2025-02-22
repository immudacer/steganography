Steganography Tool - Hide and Extract Messages in Images

This tool allows you to hide secret messages inside an image using steganography and later extract them using a password.

Features:

Hide Data: Embed a secret message inside an image along with a password.

Extract Data: Retrieve the hidden message using the correct password.

Password Protection: Ensures message security by requiring the correct password for extraction.

Looped Interface: Allows multiple hide/extract operations until the user chooses to exit.

Error Handling: Checks for valid image files before processing.

Requirements:

Python 3.x

OpenCV (cv2 library)

Installation:

Install Python if not already installed.

Install OpenCV using the following command:

pip install opencv-python

How to Use:

Run the script:

python script.py

Choose an option:

Enter 1 to hide a message in an image. (Remember the file in which the secret message is stored is stored in the original file path but with a .png file format)

Enter 2 to extract a message from an image. 

Enter 3 to exit.

Hiding Data in an Image:

Provide the file path of the image.

Enter the secret message.

Enter a passcode.

The message is embedded, and a new image file is saved with _stegano.png suffix.

Extracting Data from an Image:

Provide the file path of the steganographed image.

Enter the passcode.

If the password matches, the hidden message is displayed. Otherwise, access is denied.

Notes:

The password and message are stored within the image and must be correctly entered for retrieval.

The message is encoded using a delimiter (|END) to mark the end.

Ensure the image size is sufficient to store the message.

Disclaimer:

This tool is for educational and ethical use only. Unauthorized use for hiding malicious data is strictly discouraged.

Happy Steganography! 🔍
