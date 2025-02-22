#
import cv2
# Function to embed message into an image
def hide_data_in_image(file_path, message, password):
    img = cv2.imread(file_path)
    if img is None:
        print("Error: Could not open image file.")
        return

    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0
    message = password + '|' + message + '|END'  # Store password with message and add a delimiter

    for char in message:
        img[n, m, z] = d.get(char, 0)  # Ensure unknown chars default to 0
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    new_file_path = file_path.split('.')[0] + "_stegano.png"
    cv2.imwrite(new_file_path, img)
    print(f"Data hidden successfully in {new_file_path}")


# Function to extract message from an image
def extract_data_from_image(file_path, password):
    img = cv2.imread(file_path)
    if img is None:
        print("Error: Could not open image file.")
        return

    c = {i: chr(i) for i in range(255)}

    n, m, z = 0, 0, 0
    message = ""

    while True:
        char = c.get(int(img[n, m, z]), '?')  # Convert np.uint8 to int
        if message.endswith('|END'):
            break
        message += char
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    message = message[:-4]  # Remove '|END'
    stored_password, hidden_message = message.split('|', 1)

    if stored_password == password:
        print("Hidden message:", hidden_message)
    else:
        print("Incorrect passcode! Access denied.")


# Main program loop
while True:
    choice = input(
        "Enter 1 to hide data in a file (image), enter 2 for extracting hidden data, enter 3 to exit program: ")

    if choice == '1':
        file_path = input("Enter file path in which you want to hide data: ")
        message = input("Enter secret message you want to hide: ")
        password = input("Enter pass code: ")
        hide_data_in_image(file_path, message, password)

    elif choice == '2':
        file_path = input("Enter path of the file: ")
        password = input("Enter passcode: ")
        extract_data_from_image(file_path, password)

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
