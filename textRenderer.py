import colorsys
from PIL import Image, ImageFont, ImageDraw


class TextRenderer:

    def __init__(self, font="./NotoSansCJK-Bold.otf",
                 font_color=(0, 120, 0), color_bg=False):
        self.image = None

        # params
        self.color_bg = color_bg
        self.font_color = font_color

        # new image and font
        self.font = ImageFont.truetype(font, 30)
        return None

    def getFrameCount(self):
        return 1

    def rainbow_bg(c):
        # hue, lightness, saturation to rgb
        vals = colorsys.hls_to_rgb(round(c / 360.0, 2), 0.05, 1)
        return (int(vals[0] * 255), int(vals[1] * 255), int(vals[2] * 255))

    def draw_text(self, text_to_send):
        x, y = self.font.getsize(text_to_send)

        self.im = Image.new("RGBA", (x, y+10), "black")
        # Add padding below, because PIL sucks!
        self.draw = ImageDraw.Draw(self.im)

        self.draw.text(
            (0, 0), text_to_send, font=self.font, fill=self.font_color
        )

    def render(self, msgText):
        self.draw_text(' '.join(msgText))

    def getImage(self):
        return self.image

    def get_queue_token(self, msgToken):
        queue_token = {}
        # TODO: add possible params
        self.render(msgToken["text"])
        queue_token["image"] = [self.im]
        queue_token["frame_count"] = self.getFrameCount()
        queue_token["action"] = "scroll"
        queue_token["valid"] = True

        return queue_token
