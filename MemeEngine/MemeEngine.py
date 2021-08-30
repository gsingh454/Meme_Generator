from PIL import Image, ImageDraw, ImageFont
from time import time
from random import randrange
import os

# resizing and drawing text on the images.


class MemeEngine:
    """
    Creating an image with a quote on top of it.
    in_path {str} -- file location of the input file
    text {str} -- the quote which will be on the image
    author {str} -- the author of the quote
    width {int} -- the pixel width length of the image
    Return: str -- the file path to the output image
    """
    def __init__(self, out_path):
        self.out_path = out_path

        if not os.path.exists(out_path):
            os.makedirs(out_path)

    def make_meme(self, in_path, text, author, width=500) -> str:
        """
        Meme will be generated here using image, text and author.
        Firstly, load the file.
        Resize the image to a maximum width of 500px and maintain
        the input aspect ratio. Add the text quote to the image
        which contains the body and author at a random location
        on the image.
        Save the image generated in the tmp directory.
        Return: The path of the generated image.
        """
        img = Image.open(in_path)
        # resizing the image
        w, h = img.size
        width = max(500, width)
        r = width / w
        height = int(r * h)
        img = img.resize((width, height), Image.NEAREST)

        # put the text on top of the image
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./_data/Fonts/LilitaOne-Regular.ttf',
                                  size=20)

        # put the quote on 'random' position on the image
        row_text = randrange(30, height - 50)
        draw.text((50, row_text), str(text), font=font, fill='white')
        draw.text((50, row_text + 20), f'- {author}', font=font, fill='white')

        out_dir = os.path.join(self.out_path, f'tmp-{time()}.png')
        img.save(out_dir)
        print(f'Image saved to {out_dir}.')
        return out_dir
