from ui import UI

class brian:
    def __init__(self):
        val = UI.window_elements()

    def place_elements(self):
        # Frames:
        self.left_frame.grid(row=0, column=0)
        self.right_frame.grid(row=0, column=1)
        # Toolbar:
        self.tool_bar.grid(row=0, column=0)
        # Toolbar Items:
        ## Select image:
        self.choose_img_label.grid(column=0, row=0)
        self.choose_img_button.grid(column=1, row=0)
        ## Input text:
        self.inp_tex_label.grid(column=0, row=1)
        self.inp_tex.grid(column=1, row=1)
        self.inp_tex_button.grid(column=1, row=2)
        self.er_tab.grid(column=0, row=2)
        ## Select position:
        self.pos_label.grid(column=0, row=3)
        self.pos_frame.grid(column=1, row=3)
        ### Position Matrix:
        self.zero_zero.grid(column=0, row=0)
        self.zero_one.grid(column=0, row=1)
        self.zero_two.grid(column=0, row=2)
        self.one_zero.grid(column=1, row=0)
        self.one_one.grid(column=1, row=1)
        self.one_two.grid(column=1, row=2)
        self.two_zero.grid(column=2, row=0)
        self.two_one.grid(column=2, row=1)
        self.two_two.grid(column=2, row=2)
        ## Font:
        self.font_label.grid(column=0, row=4)
        self.font_setting_label.grid(column=0, row=5)
        ### Font toolbar:
        self.font_toolbar.grid(column=1, row=5, columnspan=2)
        #### Color toolbar:
        self.color_bar.grid(column=0, row=0)
        self.foreground_color.grid(column=0, row=0)
        self.background_color.grid(column=0, row=1)
        #### Bold, Italic and Underline toolbar:
        self.b_i_u.grid(column=1, row=0)
        self.bold.grid(column=0, row=0)
        self.italic.grid(column=1, row=0)
        self.underline.grid(column=2, row=0)
        ## Text size:
        self.text_size_menu.grid(row=6, column=1)
        self.text_size_label.grid(row=6, column=0)
        ## Rotate:
        self.rotate_label.grid(column=0, row=7)
        self.rotate_val.grid(column=1, row=7)
        self.r_scale.grid(column=1, row=8, sticky='ew', pady=10)
        ## Transparency:
        self.transparency_label.grid(column=0, row=9)
        self.transparency_val.grid(column=1, row=9)
        self.t_scale.grid(column=1, row=10, sticky='ew', pady=10)
        ## Save Image:
        self.save_button.grid(column=1, row=11)
