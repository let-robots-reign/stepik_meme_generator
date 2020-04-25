from PIL import Image, ImageDraw, ImageFont


def draw_text(image, type, text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("impact.ttf", 50)
    white_color = (255, 255, 255)
    text_width, text_height = draw.textsize(text, font)  # ширина данного текста с данным шрифтом
    y_start = 10 if type == "top" else image.height - text_height - 10  # зависит от расположения
    draw.text((image.width / 2 - text_width / 2, y_start), text, white_color, font)


def make_meme(image, top_text="", bottom_text=""):
    draw_text(image, "top", top_text.upper())
    draw_text(image, "bottom", bottom_text.upper())
    return image


def main():
    image = Image.open("templates/boromir.jpg")
    image = make_meme(image, "Нельзя так просто взять", "и сразу написать идеальное приложение")
    image.save("meme_result.jpg")
    image.show()


main()
