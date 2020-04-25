from PIL import Image, ImageDraw, ImageFont
from os import listdir


def split_text(draw, text, font, img_width):
    lines = []
    cur_word = 0
    words = text.split()
    while cur_word != len(words):
        # если даже одно слово слишком длинное, скажем об этом пользователю
        if draw.textsize(words[cur_word], font)[0] > img_width:
            print("Слово", words[cur_word], "слишком длинное для этой картинки")
            quit()

        # будем добавлять в текущую строчку слова, пока эта строчка влезает
        cur_line = []
        # пока текущая строка с прибавлением нового слова все еще вмещается
        while cur_word < len(text.split()) and draw.textsize(" ".join(cur_line) + words[cur_word], font)[0] < img_width:
            # добавляем к текущей строке новое слово
            cur_line.append(words[cur_word])
            cur_word += 1
        lines.append(" ".join(cur_line))
    return lines


def draw_outlined_text(draw, pos, text, font):
    black_color = (0, 0, 0)
    white_color = (255, 255, 255)
    draw.text((pos[0] - 3, pos[1] - 3), text, black_color, font)
    draw.text((pos[0] + 3, pos[1] + 3), text, black_color, font)
    draw.text((pos[0] + 3, pos[1] - 3), text, black_color, font)
    draw.text((pos[0] - 3, pos[1] + 3), text, black_color, font)
    draw.text(pos, text, white_color, font)


def draw_text(image, type, text):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("impact.ttf", 50)
    lines = split_text(draw, text, font, image.width)
    text_height = draw.textsize(text, font)[1]  # общая высота для каждой строки
    for i in range(len(lines)):
        text_width = draw.textsize(lines[i], font)[0]  # ширина данной строки с данным шрифтом
        if type == "top":
            y_start = text_height * i + 10
        else:
            y_start = image.height - text_height * (len(lines) - i) - 10

        draw_outlined_text(draw, (image.width / 2 - text_width / 2, y_start), lines[i], font)


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


if __name__ == "__main__":
    main()
