from PIL import Image, ImageTk, ImageFont, ImageDraw
import matplotlib.pyplot as plt

class misc:
    def __init__(self) -> None:
        self.original_image = None
        self.tk_image = None
        self.o_height = None
        self.o_width = None

    def get_resolution(self, width, height):
        for i in range(1, 20):
            if width//i < 500 and height//i < 400:
                return width//i, height//i
    

    def get_image(self, image_path):
        self.original_image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.original_image)

        self.o_width, self.o_height = self.original_image.size
    
        return self.original_image

    def put_image_on_canvas(self, im_path, l_r):

        o_im = Image.open(im_path)

        width, height = self.get_resolution(o_im.width, o_im.height)
        im = o_im.resize((width, height))

        # Put image in the window.
        l_r.image = ImageTk.PhotoImage(im)
        l_r['image'] = l_r.image
    

    def put_text_on_image(self, tex, im_label):
        
        draw = ImageDraw.Draw(self.original_image)

        watermark_image = self.tk_image.copy()
        watermark_image.show()

        x, y =int(watermark_image.width/2), int(watermark_image.height/2)
        if x > y:
            font_size = y
        elif y > x:
            font_size = x
        else:
            font_size = x

        font = ImageFont.truetype("arial.ttf", int(font_size/6))
        draw.text((x,y), tex, fill=(0, 0, 0), font=font, anchor='ms')

        plt.subplot(1, 2, 1)
        plt.title("black text")
        plt.imshow(watermark_image)

        im_label.config(image=watermark_image)
        
        