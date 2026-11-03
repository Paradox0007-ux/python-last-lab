
from PIL import Image, ImageFilter

def open_image():
    path = input("Enter image file path: ")

    try:
        img = Image.open(path).convert("RGB")
        print("Image loaded successfully!")
        print("Image Size:", img.size)
        return img

    except Exception as e:
        print("Error opening image:", e)
        return None


def grayscale(img):
    width, height = img.size
    result = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            gray = int((r + g + b) / 3)

            result.putpixel((x, y), (gray, gray, gray))

    return result


def threshold(img):
    width, height = img.size
    result = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            gray = int((r + g + b) / 3)

            if gray >= 128:
                result.putpixel((x, y), (255, 255, 255))
            else:
                result.putpixel((x, y), (0, 0, 0))

    return result


def blur_image(img):
    return img.filter(ImageFilter.BLUR)


def main():
    img = open_image()

    if img is None:
        return

    while True:
        print("\n===== IMAGE PROCESSING TOOL =====")
        print("1. Grayscale Image")
        print("2. Black and White Image")
        print("3. Blur Image")
        print("4. Save Original Image")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = grayscale(img)
            result.save("grayscale.png")
            print("Grayscale image saved as grayscale.png")

        elif choice == "2":
            result = threshold(img)
            result.save("black_white.png")
            print("Black and white image saved!")

        elif choice == "3":
            result = blur_image(img)
            result.save("blur.png")
            print("Blur image saved as blur.png")

        elif choice == "4":
            img.save("original_copy.png")
            print("Original image saved!")

        elif choice == "5":
            print("Exiting Image Processing Tool...")
            break

        else:
            print("Invalid choice! Try again.")


main()
