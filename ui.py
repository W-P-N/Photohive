from tkinter import Label, Button, Tk, Frame, Text, OptionMenu, StringVar, CENTER
from tkinter import ttk, HORIZONTAL
from math import floor
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from image_processing import misc

i_p = misc()

class style:
    bold = "\033[1m"
    underline = "\033[4m"
    italic = "\x1B[3m"
    end = "\033[0m"

class UI:

    def __init__(self):
        self.image_path = None
        self.image = None
        self.o_height = None
        self.o_width = None
        self.mod_height = None
        self.mod_width = None


    def create_ui(self):
        # Initializing window
        self.window = Tk()
        self.window.geometry("1000x600")
        self.window.maxsize(1000, 600)
        self.window.title("PhotoHive")
        
        # Left and right Frames set up.
        self.left_frame = Frame(self.window, width=450, height=500)
        self.left_frame.grid(row=0, column=0, padx=8, pady=5, sticky="w")

        self.right_frame = Frame(self.window, width=500, height=400, bg='grey')
        self.right_frame.grid(row=0, column=1, padx=8, pady=5, sticky="w")

        # Toolbar set up.
        self.tool_bar = Frame(self.left_frame, width=180, height=185, padx=10)
        self.tool_bar.grid(row=0, column=0, padx=8, pady=5, sticky="w")
        
        # Items in the toolbar - 
        ## Select Image:
        self.choose_img_label = Label(self.tool_bar, text="Choose the image to put water mark on: ")
        self.choose_img_label.grid(column=0, row=0, padx=8, pady=5, sticky="w")
        self.choose_img_button = Button(self.tool_bar, text="Choose", padx=10, command=self.get_image)
        self.choose_img_button.grid(column=1, row=0, padx=8, pady=5, sticky="w")
        ## Input text:
        self.inp_tex_label = Label(self.tool_bar, text="Enter the text you want to watermark: ")

        self.inp_tex = Text(self.tool_bar, padx=10, pady=10, height=1, width=15)
    
        self.inp_tex_button = Button(self.tool_bar, text="Get watermark", padx=5, pady=5, command=self.get_text)

        self.er_tab = Label(self.tool_bar, text="No input", fg="red")

        ## Select position:
        self.pos_label = Label(self.tool_bar, text="Select position: ")  # Text label
        
        self.pos_frame = Frame(self.tool_bar, width=200, height=200, bg="grey", padx=10, pady=10)  # Frame for matrix.
        
        ### Position Matrix:
        self.zero_zero = Button(self.pos_frame, text=" ", width=5)
        
        self.zero_one = Button(self.pos_frame, text=" ", width=5)
    
        self.zero_two = Button(self.pos_frame, text=" ", width=5)
    
        self.one_zero = Button(self.pos_frame, text=" ", width=5)
    
        self.one_one = Button(self.pos_frame, text=" ", width=5)

        self.one_two = Button(self.pos_frame, text=" ", width=5)

        self.two_zero = Button(self.pos_frame, text=" ", width=5)
    
        self.two_one = Button(self.pos_frame, text=" ", width=5)

        self.two_two = Button(self.pos_frame, text=" ", width=5)

        ## Font:
        options_font = [
            "Helvetica",
            "Baskerville",
            "Times New Roman",
            "Gotham",
            "Futura",
            "Gill Sans"
        ]
        self.defalut_val_opt_font = StringVar()
        self.defalut_val_opt_font.set("Default")
        self.font_label = Label(self.tool_bar, text="Choose Font: ")
        
        self.font_dropdown_label = OptionMenu(self.tool_bar , self.defalut_val_opt_font, *options_font)
        
        
        self.font_setting_label = Label(self.tool_bar, text="Font settings:")
        
        ### Font toolbar:
        self.font_toolbar = Frame(self.tool_bar, bg="grey")

        #### Color toolbar:
        self.color_bar = Frame(self.font_toolbar)
        

        self.foreground_color = Button(self.color_bar, text="FG", command=askcolor, width=5)
    

        self.background_color = Button(self.font_toolbar, text="BG", command=askcolor, width=5)
    

        #### Bold, Italic and Underline toolbar:
        self.b_i_u = Frame(self.font_toolbar)
        
        self.bold_text = style.bold + "B" + style.end
        self.bold = Button(self.b_i_u, text="B", width=5)
    
        self.italic_text = style.italic + "I" + style.end
        self.italic = Button(self.b_i_u, text="I", width=5)
    
        self.underline_text = style.underline + "U" + style.end
        self.underline = Button(self.b_i_u, text="U", width=5)
        

        ## Text size:
        options_size = [
            10,
            11,
            12,
            14,
            16,
            18,
            20,
            24,
            26,
            28,
            36,
            48,
            72
        ]
        self.defalut_val_opt_size = StringVar()
        self.defalut_val_opt_size.set(14)
        self.text_size_menu = OptionMenu(self.tool_bar, self.defalut_val_opt_size, *options_size)
        
        self.text_size_label = Label(self.tool_bar, text="Font Size:")
        

        ## Rotate:
        self.rotate_label = Label(self.tool_bar, text="Rotate text: ")
        
        self.rotate_val = Label(self.tool_bar, text="0")

        self.r_scale = ttk.Scale(self.tool_bar, from_=0, to=359, orient=HORIZONTAL, command=lambda val:self.change_rotate_label(val))
        self.r_scale.set(0)
        ## Transparency:
        self.transparency_label = Label(self.tool_bar, text="Transparency: ")
    
        self.transparency_val = Label(self.tool_bar, text="100")
    
        self.t_scale = ttk.Scale(self.tool_bar, from_=0, to=100, orient=HORIZONTAL, command=lambda val:self.change_transparency_label(val))
        self.t_scale.set(100)
      
        ## Save Image button:
        self.save_button = Button(self.tool_bar, text="Save Image", width=10, pady=5)


        self.window.mainloop()
    

    # Function to change rotation of text depending on slider value.
    def change_rotate_label(self, val):
        self.rotate_val.config(text=str(floor(float(val))) + " Deg")
    

    # Function to change transparency of text depending on slider value.
    def change_transparency_label(self, val):
        self.transparency_val.config(text=str(floor(float(val))) + " %")

    
    # Function to show other options:
    def get_image(self):
        self.image_path = askopenfilename(filetypes=(('*.jpg', 'jpg'), ('*.jpeg', '.jpeg'), ('*.png', '.png'), ('*.heic', 'heic'), ('Image File')))
        # Create a frame for the image.
        self.l_r = Label(self.right_frame)
        self.l_r.grid(row=0,column=0, padx=20, pady=5)
        self.l_r.place(relx=0.5, rely=0.5, anchor=CENTER)

        i_p.put_image_on_canvas(self.image_path, l_r=self.l_r)  # Returns image and original dimensions of the image to save the image.

        ## Input text:
        self.inp_tex_label.grid(column=0, row=1, padx=8, pady=5, sticky="w")
        self.inp_tex.grid(column=1, row=1, padx=8, pady=5, sticky="w")
        self.inp_tex_button.grid(column=1, row=2, padx=8, pady=5, sticky="w")
        
    


    # Function to get text:
    def get_text(self):
        tex = self.inp_tex.get(1.0, "end-1c")
        if len(tex) == 0 or tex.isspace():
            self.er_tab.grid(column=0, row=2)
        else:
            self.er_tab.grid_remove()
            # Put text on image
            i_p.put_text_on_image(tex, self.l_r)

            # Select position:
            self.pos_label.grid(column=0, row=3, padx=8, pady=5, sticky="w")
            self.pos_frame.grid(column=1, row=3, padx=8, pady=5, sticky="w")
            ## Position Matrix:
            self.zero_zero.grid(column=0, row=0)
            self.zero_one.grid(column=0, row=1)
            self.zero_two.grid(column=0, row=2)
            self.one_zero.grid(column=1, row=0)
            self.one_one.grid(column=1, row=1)
            self.one_two.grid(column=1, row=2)
            self.two_zero.grid(column=2, row=0)
            self.two_one.grid(column=2, row=1)
            self.two_two.grid(column=2, row=2)