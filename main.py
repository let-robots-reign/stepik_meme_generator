from PIL import Image, ImageDraw, ImageFont
from os import listdir


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


def input_parameters():
    print("Введите цифру - шаблон для мема")
    files = listdir("templates")
    for i in range(len(files)):
        print(files[i], "-", i + 1)
    digit = int(input())
    if digit < 1 or digit - 1 > len(files):
        print("Вы ввели неверный номер шаблона")
        quit()
    top_text = input("Введите текст сверху (Enter, чтобы пропустить): ")
    bottom_text = input("Введите текст снизу (Enter, чтобы пропустить): ")
    return files[digit - 1], top_text, bottom_text


def main():
    image_name, top_text, bottom_text = input_parameters()
    image = Image.open("templates/{}".format(image_name))
    image = make_meme(image, top_text, bottom_text)
    image.save("meme_result.jpg")
    image.show()


main()
