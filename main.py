from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from constants import *
import logging
import logging.config
from os import path
import datetime
from tree_algorithms import *


class MainWindow:

    def resize(self, event):
        e = event
        if str(type(event.widget)) == "<class 'tkinter.Tk'>":
            print("found")
            if (self.win_width != e.width) or (self.win_height != e.height):
                print("changed")
                self.win_width = e.width
                self.win_height = e.height
                print(f"new size: {e.width}, {e.height}")
                if self.image and self.img:
                    width, height = self.img.size
                    ratio = self.get_ratio(width, height)
                    ratio = 1.2
                    ratio2 = max(width * .9 / e.width, height * .9 / (e.height - 40))
                    ratio = ratio * ratio2
                    self.change_image(self.img, width, height, ratio, False)
                    print(f"image resized")

    def __init__(self):
        self.algo_result = None
        self.canvas = None
        self.frame_strip = None
        self.image = None
        self.top_frame_height = 0
        self.img = None
        self.root = None

        self.win_width = 0
        self.win_height = 0

        self.logger = logging.getLogger(__name__)

        root = Tk()
        root.bind("<Configure>", self.resize)

        root.title(APP_TITLE)
        root.geometry('1000x800')
        self.root = root
        self.setup_controls()

        self.window_width = 10
        self.window_height = 10

    @staticmethod
    def mb(msg):
        messagebox.showinfo(MESSAGEBOX_TITLE, msg)

    @staticmethod
    def get_ratio(width, height):
        ratio1 = width / 720
        ratio2 = height / 720
        ratio = min(ratio1, ratio2)
        # avoid possible divide by zero error
        if ratio == 0:
            ratio = 0.1
        return ratio

    def change_image(self, img, width, height, ratio, resize_now):
        resized = img.resize((int(width / ratio), int(height / ratio)))

        if resize_now:
            self.root.geometry(str(int(width / ratio) + 0) + "x" + str(int(height / ratio) + self.top_frame_height + 10))
        self.image = ImageTk.PhotoImage(resized)
        self.canvas.create_image(int(width / (ratio * 2)) + 0, int(height / (ratio * 2)) + 0, image=self.image)

    def run_algorithm(self):
        ta = TreeAlgorithms()
        #res = ta.do_same_test()
        res = ta.do_level_traversal()
        self.algo_result = res
        print(res)
    
    def view_properties(self):
        top = Toplevel(self.root)
        top.title(PROPERTIES_WINDOW_TITLE)
        top["bg"] = '#4284f5'
        top.mainloop()

    @staticmethod
    def get_image_file():
        file_path = filedialog.askopenfilename(initialdir=INITIAL_DIRECTORY, title=SELECT_IMAGE_TEXT,
                                               filetypes=(("jpeg files", "*.jpg"), ("gif files", "*.gif*"),
                                                          ("png files", "*.png")))
        return file_path

    def open_image(self):
        file_path = self.get_image_file()
        if file_path == '':
            return

        self.logger.info('opened file: ' + file_path)
        # self.logger.info(f'opened file: {file_path}')
        self.set_title(APP_TITLE_PREFIX + file_path)

        self.img = Image.open(file_path)
        width, height = self.img.size
        ratio = self.get_ratio(width, height)
        self.change_image(self.img, width, height, ratio, True)

    def set_title(self, file_path):
        file_name = os.path.basename(file_path)
        self.root.title(APP_TITLE_PREFIX + file_name)

    def setup_controls(self):
        # try:
        #     n = 1 / 0
        # except BaseException as e:
        #     self.mb('some info')
        self.frame_strip = Frame(self.root)
        self.frame_strip.pack(pady=5)

        open_btn = Button(
            self.frame_strip,
            text='Open',
            command=self.open_image
        )
        open_btn.pack(side=LEFT, padx=(10, 5))
        properties_btn = Button(
            self.frame_strip,
            text='Properties',
            command=self.view_properties
        )
        properties_btn.pack(side=LEFT)
        
        algo_btn = Button(
            self.frame_strip,
            text='Run algorithm',
            command=self.run_algorithm
        )
        algo_btn.pack(side=LEFT)
        self.frame_strip.update()
        self.top_frame_height = self.frame_strip.winfo_height()

        canvas = Canvas(self.root, width=2000, height=2000)
        canvas.pack()

        self.canvas = canvas

    def main_loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    path1 = os.getcwd()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)8.8s] %(message)s",
        handlers=[logging.StreamHandler(),
                  logging.FileHandler(f'log/{datetime.datetime.now().isoformat().replace(":", "-")}.log',
                                      encoding='utf-8')],
    )

    frame = MainWindow()
    frame.main_loop()
