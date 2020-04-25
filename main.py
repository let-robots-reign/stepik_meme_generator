from PIL import Image, ImageDraw, ImageFont


def make_meme(image, top_text="", bottom_text=""):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("impact.ttf", 50)
    white_color = (255, 255, 255)
    draw.text((10, 10), top_text, white_color, font)
    return image


def main():
    image = Image.open("templates/boromir.jpg")
    image = make_meme(image, "Sample Text")
    image.save("meme_result.jpg")
    image.show()


main()
